## Build and package

    $ conan create xpilot-project/stable
    
## Add remote

    $ conan remote add xpilot-project "https://api.bintray.com/conan/jshannon/xpilot-project"
    
## Upload

    $ conan upload speexdsp/0.1@xpilot-project/stable --all -r xpilot-project