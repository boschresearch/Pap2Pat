# DESCRIPTION

## FIELD OF THE INVENTION

- define field of invention

## BACKGROUND OF THE INVENTION

- describe video streaming evolution
- provide statistics on video streaming traffic
- explain video stream structure
- describe video transcoding process
- discuss video transcoding levels
- explain bit rate adjustment
- describe spatial resolution reduction
- describe temporal resolution reduction
- discuss video compression standard conversion

## SUMMARY OF THE INVENTION

- summarize CVSS architecture

## DETAILED DESCRIPTION

- introduce CVSS architecture for on-demand video transcoding in the cloud
- describe six main components of CVSS architecture
- explain video splitter component
- motivate close-GOP type processing
- introduce transcoding task scheduler
- describe goal of scheduler
- explain GOP interleaving in scheduling queue
- describe transcoding virtual machines (VMs)
- explain local queue preloading
- introduce elasticity manager (EM)
- describe dynamic resource provisioning policies
- explain video merger component
- introduce caching policy
- describe QoS-aware transcoding scheduling method
- explain GOP batching and startup queue
- describe task completion time estimation
- explain priority assignment to GOP tasks
- introduce dynamic resource provisioning policy overview
- describe periodic resource provisioning policy
- explain remedial resource provisioning policy
- describe performance evaluation of CVSS architecture
- show impact of QoS-aware scheduling method
- evaluate impact of queuing policy
- compare dynamic and static resource provisioning policies
- analyze cost and QoS trade-off using Pareto front analysis

