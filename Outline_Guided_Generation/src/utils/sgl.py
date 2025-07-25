import concurrent.futures
import multiprocessing
import time
from typing import Any, Callable

import requests
from sglang.global_config import global_config
from sglang.lang.interpreter import (
    ProgramState,
    ProgramStateGroup,
    cache_program,
    run_program,
)

from src.utils.general import get_logger

log = get_logger(__file__)


def return_exception(f) -> Callable:
    def inner(*args: tuple[Any, ...], **kwargs) -> Any:
        try:
            return f(*args, **kwargs)
        except BaseException as e:
            log.exception("Exception in generation function")
            return e

    return inner


def run_program_batch_generator(
    program, backend, batch_arguments, default_sampling_para, num_threads, progress_bar
):
    if hasattr(backend, "endpoint"):
        backend = backend.endpoint

    # Pre-cache the common prefix for a batch. The prefix is extracted by tracing the program.
    if global_config.enable_precache_with_tracing and len(batch_arguments) > 1:
        cache_program(program, backend)

    # Run all programs
    if num_threads == "auto":
        num_threads = max(96, multiprocessing.cpu_count() * 16)
    num_threads = min(num_threads, len(batch_arguments))

    # Execute each run_program call and yield results as they become available
    if num_threads == 1:
        for arguments in batch_arguments:
            yield (
                arguments,
                run_program(
                    program,
                    backend,
                    (),
                    arguments,
                    default_sampling_para,
                    False,
                    True,
                ),
            )
    else:
        with concurrent.futures.ThreadPoolExecutor(num_threads) as executor:
            # Use a dictionary to map futures to their corresponding arguments
            future_to_arguments = {
                executor.submit(
                    run_program,
                    program,
                    backend,
                    (),
                    arguments,
                    default_sampling_para,
                    False,
                    True,
                ): arguments
                for arguments in batch_arguments
            }

            # Asynchronously yield results as they complete
            for future in concurrent.futures.as_completed(future_to_arguments):
                try:
                    yield future_to_arguments[future], future.result()

                except concurrent.futures.TimeoutError as e:
                    log.exception("Thread timed out")
                    yield future_to_arguments[future], e

                except Exception as e:
                    log.exception("Exception in thread")
                    yield future_to_arguments[future], e


def get_model_info(port: int, max_startup_time: int) -> dict:
    start = time.time()
    while True:
        try:
            r = requests.get(f"http://localhost:{port}/get_model_info")
            r.raise_for_status()
            return r.json()

        except Exception as e:
            if time.time() - start > max_startup_time:
                raise e
            log.warning(
                f"Couldn't get model info: {e}. Retrying in 3 secs. max_startup_time: {max_startup_time}"
            )
            time.sleep(3)


class MyProgramState(ProgramState):
    chunk_forks: ProgramStateGroup
