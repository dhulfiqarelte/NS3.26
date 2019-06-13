#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.26-aodv-optimized', 'build/src/bridge/examples/ns3.26-csma-bridge-optimized', 'build/src/bridge/examples/ns3.26-csma-bridge-one-hop-optimized', 'build/src/buildings/examples/ns3.26-buildings-pathloss-profiler-optimized', 'build/src/config-store/examples/ns3.26-config-store-save-optimized', 'build/src/core/examples/ns3.26-main-callback-optimized', 'build/src/core/examples/ns3.26-sample-simulator-optimized', 'build/src/core/examples/ns3.26-main-ptr-optimized', 'build/src/core/examples/ns3.26-main-random-variable-optimized', 'build/src/core/examples/ns3.26-main-random-variable-stream-optimized', 'build/src/core/examples/ns3.26-sample-random-variable-optimized', 'build/src/core/examples/ns3.26-sample-random-variable-stream-optimized', 'build/src/core/examples/ns3.26-command-line-example-optimized', 'build/src/core/examples/ns3.26-hash-example-optimized', 'build/src/core/examples/ns3.26-test-string-value-formatting-optimized', 'build/src/core/examples/ns3.26-main-test-sync-optimized', 'build/src/csma/examples/ns3.26-csma-one-subnet-optimized', 'build/src/csma/examples/ns3.26-csma-broadcast-optimized', 'build/src/csma/examples/ns3.26-csma-packet-socket-optimized', 'build/src/csma/examples/ns3.26-csma-multicast-optimized', 'build/src/csma/examples/ns3.26-csma-raw-ip-socket-optimized', 'build/src/csma/examples/ns3.26-csma-ping-optimized', 'build/src/csma-layout/examples/ns3.26-csma-star-optimized', 'build/src/dsdv/examples/ns3.26-dsdv-manet-optimized', 'build/src/dsr/examples/ns3.26-dsr-optimized', 'build/src/energy/examples/ns3.26-li-ion-energy-source-optimized', 'build/src/energy/examples/ns3.26-rv-battery-model-test-optimized', 'build/src/energy/examples/ns3.26-basic-energy-model-test-optimized', 'build/src/fd-net-device/examples/ns3.26-dummy-network-optimized', 'build/src/fd-net-device/examples/ns3.26-fd2fd-onoff-optimized', 'build/src/fd-net-device/examples/ns3.26-realtime-dummy-network-optimized', 'build/src/fd-net-device/examples/ns3.26-realtime-fd2fd-onoff-optimized', 'build/src/fd-net-device/examples/ns3.26-fd-emu-ping-optimized', 'build/src/fd-net-device/examples/ns3.26-fd-emu-udp-echo-optimized', 'build/src/fd-net-device/examples/ns3.26-fd-emu-onoff-optimized', 'build/src/fd-net-device/examples/ns3.26-fd-tap-ping-optimized', 'build/src/fd-net-device/examples/ns3.26-fd-tap-ping6-optimized', 'build/src/internet/examples/ns3.26-main-simple-optimized', 'build/src/lr-wpan/examples/ns3.26-lr-wpan-packet-print-optimized', 'build/src/lr-wpan/examples/ns3.26-lr-wpan-phy-test-optimized', 'build/src/lr-wpan/examples/ns3.26-lr-wpan-data-optimized', 'build/src/lr-wpan/examples/ns3.26-lr-wpan-error-model-plot-optimized', 'build/src/lr-wpan/examples/ns3.26-lr-wpan-error-distance-plot-optimized', 'build/src/lte/examples/ns3.26-lena-cqi-threshold-optimized', 'build/src/lte/examples/ns3.26-lena-dual-stripe-optimized', 'build/src/lte/examples/ns3.26-lena-fading-optimized', 'build/src/lte/examples/ns3.26-lena-intercell-interference-optimized', 'build/src/lte/examples/ns3.26-lena-pathloss-traces-optimized', 'build/src/lte/examples/ns3.26-lena-profiling-optimized', 'build/src/lte/examples/ns3.26-lena-rem-optimized', 'build/src/lte/examples/ns3.26-lena-rem-sector-antenna-optimized', 'build/src/lte/examples/ns3.26-lena-rlc-traces-optimized', 'build/src/lte/examples/ns3.26-lena-simple-optimized', 'build/src/lte/examples/ns3.26-lena-simple-epc-optimized', 'build/src/lte/examples/ns3.26-lena-deactivate-bearer-optimized', 'build/src/lte/examples/ns3.26-lena-x2-handover-optimized', 'build/src/lte/examples/ns3.26-lena-x2-handover-measures-optimized', 'build/src/lte/examples/ns3.26-lena-frequency-reuse-optimized', 'build/src/lte/examples/ns3.26-lena-distributed-ffr-optimized', 'build/src/lte/examples/ns3.26-lena-uplink-power-control-optimized', 'build/src/mesh/examples/ns3.26-mesh-optimized', 'build/src/mobility/examples/ns3.26-main-grid-topology-optimized', 'build/src/mobility/examples/ns3.26-main-random-topology-optimized', 'build/src/mobility/examples/ns3.26-main-random-walk-optimized', 'build/src/mobility/examples/ns3.26-mobility-trace-example-optimized', 'build/src/mobility/examples/ns3.26-ns2-mobility-trace-optimized', 'build/src/mobility/examples/ns3.26-bonnmotion-ns2-example-optimized', 'build/src/mpi/examples/ns3.26-simple-distributed-optimized', 'build/src/mpi/examples/ns3.26-third-distributed-optimized', 'build/src/mpi/examples/ns3.26-nms-p2p-nix-distributed-optimized', 'build/src/mpi/examples/ns3.26-simple-distributed-empty-node-optimized', 'build/src/netanim/examples/ns3.26-dumbbell-animation-optimized', 'build/src/netanim/examples/ns3.26-grid-animation-optimized', 'build/src/netanim/examples/ns3.26-star-animation-optimized', 'build/src/netanim/examples/ns3.26-wireless-animation-optimized', 'build/src/netanim/examples/ns3.26-uan-animation-optimized', 'build/src/netanim/examples/ns3.26-colors-link-description-optimized', 'build/src/netanim/examples/ns3.26-resources-counters-optimized', 'build/src/network/examples/ns3.26-main-packet-header-optimized', 'build/src/network/examples/ns3.26-main-packet-tag-optimized', 'build/src/network/examples/ns3.26-packet-socket-apps-optimized', 'build/src/nix-vector-routing/examples/ns3.26-nix-simple-optimized', 'build/src/nix-vector-routing/examples/ns3.26-nms-p2p-nix-optimized', 'build/src/olsr/examples/ns3.26-simple-point-to-point-olsr-optimized', 'build/src/olsr/examples/ns3.26-olsr-hna-optimized', 'build/src/point-to-point/examples/ns3.26-main-attribute-value-optimized', 'build/src/propagation/examples/ns3.26-main-propagation-loss-optimized', 'build/src/propagation/examples/ns3.26-jakes-propagation-model-example-optimized', 'build/src/sixlowpan/examples/ns3.26-example-sixlowpan-optimized', 'build/src/sixlowpan/examples/ns3.26-example-ping-lr-wpan-optimized', 'build/src/spectrum/examples/ns3.26-adhoc-aloha-ideal-phy-optimized', 'build/src/spectrum/examples/ns3.26-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-optimized', 'build/src/spectrum/examples/ns3.26-adhoc-aloha-ideal-phy-with-microwave-oven-optimized', 'build/src/spectrum/examples/ns3.26-tv-trans-example-optimized', 'build/src/spectrum/examples/ns3.26-tv-trans-regional-example-optimized', 'build/src/stats/examples/ns3.26-gnuplot-example-optimized', 'build/src/stats/examples/ns3.26-double-probe-example-optimized', 'build/src/stats/examples/ns3.26-time-probe-example-optimized', 'build/src/stats/examples/ns3.26-gnuplot-aggregator-example-optimized', 'build/src/stats/examples/ns3.26-gnuplot-helper-example-optimized', 'build/src/stats/examples/ns3.26-file-aggregator-example-optimized', 'build/src/stats/examples/ns3.26-file-helper-example-optimized', 'build/src/tap-bridge/examples/ns3.26-tap-csma-optimized', 'build/src/tap-bridge/examples/ns3.26-tap-csma-virtual-machine-optimized', 'build/src/tap-bridge/examples/ns3.26-tap-wifi-virtual-machine-optimized', 'build/src/tap-bridge/examples/ns3.26-tap-wifi-dumbbell-optimized', 'build/src/topology-read/examples/ns3.26-topology-example-sim-optimized', 'build/src/traffic-control/examples/ns3.26-red-tests-optimized', 'build/src/traffic-control/examples/ns3.26-red-vs-ared-optimized', 'build/src/traffic-control/examples/ns3.26-adaptive-red-tests-optimized', 'build/src/traffic-control/examples/ns3.26-pfifo-vs-red-optimized', 'build/src/traffic-control/examples/ns3.26-codel-vs-pfifo-basic-test-optimized', 'build/src/traffic-control/examples/ns3.26-codel-vs-pfifo-asymmetric-optimized', 'build/src/traffic-control/examples/ns3.26-pie-example-optimized', 'build/src/uan/examples/ns3.26-uan-cw-example-optimized', 'build/src/uan/examples/ns3.26-uan-rc-example-optimized', 'build/src/virtual-net-device/examples/ns3.26-virtual-net-device-optimized', 'build/src/wave/examples/ns3.26-wave-simple-80211p-optimized', 'build/src/wave/examples/ns3.26-wave-simple-device-optimized', 'build/src/wave/examples/ns3.26-vanet-routing-compare-optimized', 'build/src/wifi/examples/ns3.26-wifi-phy-test-optimized', 'build/src/wifi/examples/ns3.26-test-interference-helper-optimized', 'build/src/wifi/examples/ns3.26-ideal-wifi-manager-example-optimized', 'build/src/wifi/examples/ns3.26-minstrel-ht-wifi-manager-example-optimized', 'build/src/wifi/examples/ns3.26-wifi-phy-configuration-optimized', 'build/src/wimax/examples/ns3.26-wimax-ipv4-optimized', 'build/src/wimax/examples/ns3.26-wimax-multicast-optimized', 'build/src/wimax/examples/ns3.26-wimax-simple-optimized', 'build/examples/udp/ns3.26-udp-echo-optimized', 'build/examples/tcp/ns3.26-tcp-large-transfer-optimized', 'build/examples/tcp/ns3.26-tcp-nsc-lfn-optimized', 'build/examples/tcp/ns3.26-tcp-nsc-zoo-optimized', 'build/examples/tcp/ns3.26-tcp-star-server-optimized', 'build/examples/tcp/ns3.26-star-optimized', 'build/examples/tcp/ns3.26-tcp-bulk-send-optimized', 'build/examples/tcp/ns3.26-tcp-pcap-nanosec-example-optimized', 'build/examples/tcp/ns3.26-tcp-nsc-comparison-optimized', 'build/examples/tcp/ns3.26-tcp-variants-comparison-optimized', 'build/examples/wireless/ns3.26-mixed-wireless-optimized', 'build/examples/wireless/ns3.26-wifi-adhoc-optimized', 'build/examples/wireless/ns3.26-wifi-clear-channel-cmu-optimized', 'build/examples/wireless/ns3.26-wifi-ap-optimized', 'build/examples/wireless/ns3.26-wifi-wired-bridging-optimized', 'build/examples/wireless/ns3.26-multirate-optimized', 'build/examples/wireless/ns3.26-wifi-simple-adhoc-optimized', 'build/examples/wireless/ns3.26-wifi-simple-adhoc-grid-optimized', 'build/examples/wireless/ns3.26-wifi-simple-infra-optimized', 'build/examples/wireless/ns3.26-wifi-simple-interference-optimized', 'build/examples/wireless/ns3.26-wifi-blockack-optimized', 'build/examples/wireless/ns3.26-ofdm-validation-optimized', 'build/examples/wireless/ns3.26-ofdm-ht-validation-optimized', 'build/examples/wireless/ns3.26-ofdm-vht-validation-optimized', 'build/examples/wireless/ns3.26-wifi-hidden-terminal-optimized', 'build/examples/wireless/ns3.26-ht-wifi-network-optimized', 'build/examples/wireless/ns3.26-vht-wifi-network-optimized', 'build/examples/wireless/ns3.26-wifi-timing-attributes-optimized', 'build/examples/wireless/ns3.26-wifi-sleep-optimized', 'build/examples/wireless/ns3.26-power-adaptation-distance-optimized', 'build/examples/wireless/ns3.26-power-adaptation-interference-optimized', 'build/examples/wireless/ns3.26-rate-adaptation-distance-optimized', 'build/examples/wireless/ns3.26-wifi-aggregation-optimized', 'build/examples/wireless/ns3.26-simple-ht-hidden-stations-optimized', 'build/examples/wireless/ns3.26-80211n-mimo-optimized', 'build/examples/wireless/ns3.26-mixed-bg-network-optimized', 'build/examples/wireless/ns3.26-wifi-tcp-optimized', 'build/examples/wireless/ns3.26-80211e-txop-optimized', 'build/examples/wireless/ns3.26-wifi-spectrum-per-example-optimized', 'build/examples/wireless/ns3.26-wifi-spectrum-per-interference-optimized', 'build/examples/wireless/ns3.26-wifi-spectrum-saturation-example-optimized', 'build/examples/traffic-control/ns3.26-traffic-control-optimized', 'build/examples/traffic-control/ns3.26-queue-discs-benchmark-optimized', 'build/examples/realtime/ns3.26-realtime-udp-echo-optimized', 'build/examples/socket/ns3.26-socket-bound-static-routing-optimized', 'build/examples/socket/ns3.26-socket-bound-tcp-static-routing-optimized', 'build/examples/socket/ns3.26-socket-options-ipv4-optimized', 'build/examples/socket/ns3.26-socket-options-ipv6-optimized', 'build/examples/matrix-topology/ns3.26-matrix-topology-optimized', 'build/examples/tutorial/ns3.26-hello-simulator-optimized', 'build/examples/tutorial/ns3.26-first-optimized', 'build/examples/tutorial/ns3.26-second-optimized', 'build/examples/tutorial/ns3.26-third-optimized', 'build/examples/tutorial/ns3.26-fourth-optimized', 'build/examples/tutorial/ns3.26-fifth-optimized', 'build/examples/tutorial/ns3.26-sixth-optimized', 'build/examples/tutorial/ns3.26-seventh-optimized', 'build/examples/routing/ns3.26-dynamic-global-routing-optimized', 'build/examples/routing/ns3.26-static-routing-slash32-optimized', 'build/examples/routing/ns3.26-global-routing-slash32-optimized', 'build/examples/routing/ns3.26-global-injection-slash32-optimized', 'build/examples/routing/ns3.26-simple-global-routing-optimized', 'build/examples/routing/ns3.26-simple-alternate-routing-optimized', 'build/examples/routing/ns3.26-mixed-global-routing-optimized', 'build/examples/routing/ns3.26-simple-routing-ping6-optimized', 'build/examples/routing/ns3.26-manet-routing-compare-optimized', 'build/examples/routing/ns3.26-ripng-simple-network-optimized', 'build/examples/routing/ns3.26-rip-simple-network-optimized', 'build/examples/routing/ns3.26-global-routing-multi-switch-plus-router-optimized', 'build/examples/naming/ns3.26-object-names-optimized', 'build/examples/stats/ns3.26-wifi-example-sim-optimized', 'build/examples/ipv6/ns3.26-icmpv6-redirect-optimized', 'build/examples/ipv6/ns3.26-ping6-optimized', 'build/examples/ipv6/ns3.26-radvd-optimized', 'build/examples/ipv6/ns3.26-radvd-two-prefix-optimized', 'build/examples/ipv6/ns3.26-test-ipv6-optimized', 'build/examples/ipv6/ns3.26-fragmentation-ipv6-optimized', 'build/examples/ipv6/ns3.26-fragmentation-ipv6-two-MTU-optimized', 'build/examples/ipv6/ns3.26-loose-routing-ipv6-optimized', 'build/examples/ipv6/ns3.26-wsn-ping6-optimized', 'build/examples/error-model/ns3.26-simple-error-model-optimized', 'build/examples/udp-client-server/ns3.26-udp-client-server-optimized', 'build/examples/udp-client-server/ns3.26-udp-trace-client-server-optimized', 'build/examples/energy/ns3.26-energy-model-example-optimized', 'build/examples/energy/ns3.26-energy-model-with-harvesting-example-optimized', 'build/scratch/ns3.26-scratch-simulator-optimized', 'build/scratch/subdir/ns3.26-subdir-optimized', 'build/scratch/ns3.26-first-optimized']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'mixed-wireless.py', 'wifi-ap.py', 'realtime-udp-echo.py', 'first.py', 'second.py', 'third.py', 'simple-routing-ping6.py']

