# DESCRIPTION

## TECHNICAL FIELD

- relate to machine learning systems for document summarization

## BACKGROUND

- introduce document summarization and its challenges

## DETAILED DESCRIPTION

- define abstractive summarization and its limitations
- introduce entity coverage precision metric for faithfulness

### Systems for Abstractive Summarization

- introduce system for abstractive summarization
- describe pre-processing module
- generate article-summary pairs
- compute entity coverage precision metric
- determine pseudo label for faithfulness
- prepend pseudo label to article
- generate output summary conditioned on article and pseudo label
- update summarization model based on training objective
- describe entity coverage precision module
- compute entity coverage precision metric
- describe pseudo labeling module
- determine pseudo label for faithfulness
- describe summarization module
- generate output summary conditioned on article and pseudo label
- describe faithfulness control code
- generate control code for each training document
- compute entity coverage precision metric
- quantize precision metric into discrete bins
- represent each bin with special token control code
- prepend control code to input document
- generate faithful summaries during inference

## EXAMPLES

### Example 1: Experimental Methods and Results

- introduce experimental setup
- describe datasets used
- explain evaluation metrics
- compare with baseline methods
- describe implementation details
- present results on summary quality
- present results on summary faithfulness
- show example of generated summary
- compare with state-of-the-art methods
- study effect of controllable Wikipedia intermediate pre-training
- present human evaluation results
- analyze distribution of entities in generated summaries
- investigate effect of control codes on model performance

