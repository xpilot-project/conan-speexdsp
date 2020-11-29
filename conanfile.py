from conans import ConanFile, CMake, tools

class SpeexdspConan(ConanFile):
    name = "speexdsp"
    version = "0.1"
    license = "BSD-Like"
    author = "Justin Shannon"
    url = "https://github.com/xpilot-project/speexdsp"
    description = "SpeexDSP Audio Processing Library"
    topics = ("audio preprocessing", "audio", "sound")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/xpilot-project/speexdsp.git")
    
    def _configure_cmake(self):
        cmake = CMake(self, parallel=False)
        cmake.configure(source_folder="speexdsp")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="speexdsp/include")
        self.copy("speexdsp_config_types.h", dst="include/speex", src="include/speex", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.exp", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["speexdsp"]

