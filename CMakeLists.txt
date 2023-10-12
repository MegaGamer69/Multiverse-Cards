cmake_minimum_required(VERSION 3.5)
project(MultiverseCards LANGUAGES CXX)

set(CMAKE_MODULE_PATH ../FindSFML.cmake)
set(SFML_DIR ./app/main/src/include/SFML/SFMLConfig.cmake)
find_package(SFML 2.6 REQUIRED COMPONENTS sfml-graphics sfml-window sfml-audio ${CMAKE_MODULE_PATH})

add_executable(MultiverseCards ./app/main/src/Main.cpp)

target_link_libraries(MultiverseCards sfml-system sfml-window sfml-graphics)