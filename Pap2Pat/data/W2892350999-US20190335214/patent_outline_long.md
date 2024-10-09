# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- introduce video streaming
- describe evolution of video watching
- cite internet traffic statistics
- explain video stream structure
- describe GOP types
- explain video content conversion
- define video transcoding
- describe video transcoding levels
- explain video transcoding challenges
- cite research on video transcoding
- describe bit rate adjustment
- describe spatial resolution reduction
- describe temporal resolution reduction
- describe video compression standard conversion
- explain limitations of client-side transcoding
- describe storage-based approach limitations
- explain cloud resource utilization challenges
- describe QoS demands of video streams

## SUMMARY OF THE INVENTION

- introduce CVSS architecture
- describe scheduling method and provisioning policy
- summarize system benefits

## DETAILED DESCRIPTION

- introduce CVSS architecture for on-demand video transcoding in the cloud
- describe six main components of CVSS architecture
- explain video splitter component
- define GOP and its deadline
- describe transcoding task scheduler
- explain goal of scheduler
- describe transcoding virtual machines (VMs)
- explain elasticity manager (EM)
- describe video merger component
- explain caching policy
- introduce QoS-aware transcoding scheduling method
- describe transcoder scheduler architecture
- explain batching of GOPs in a queue
- describe startup queue
- explain calculation of GOP deadline
- describe estimation of transcoding execution time
- explain consideration of randomness in execution time
- describe calculation of task completion time
- explain priority assignment to GOP tasks
- describe queuing policy of batch queue
- introduce dynamic resource provisioning policy
- describe goal of provisioning policy
- explain "scale up early and scale down slowly" principle
- describe periodic resource provisioning policy
- explain prediction of deadline miss rate
- describe decision making on allocating new VMs
- explain variation of deadline miss rate
- describe remedial resource provisioning policy
- explain quick prediction of system state
- describe correlation between startup queue size and deadline miss rate
- explain calculation of number of VMs to allocate
- describe experiment results of remedial policy
- introduce performance evaluation
- describe impact of QoS-aware scheduling method
- explain experiment setup for QoS-aware scheduling
- describe results of QoS-aware scheduling experiment
- explain impact of queuing policy
- describe experiment setup for queuing policy
- describe results of queuing policy experiment
- compare queuing policies with static and dynamic provisioning
- describe impact of dynamic versus static resource provisioning policy
- explain experiment setup for dynamic vs static provisioning
- describe results of dynamic vs static provisioning experiment
- explain impact of remedial resource provisioning policy
- describe experiment setup for remedial policy
- describe results of remedial policy experiment
- introduce Pareto analysis for cost and QoS trade-off
- describe Pareto optimal front analysis
- explain relationship between cost and QoS violation
- describe optimal range for β
- conclude with features, advantages, and characteristics of the invention

