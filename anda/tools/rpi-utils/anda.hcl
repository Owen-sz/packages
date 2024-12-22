project pkg {
    arches = ["aarch64"]
	rpm {
		spec = "rpi-utils.spec"
	}
	labels {
	   nightly = 1
	}
}