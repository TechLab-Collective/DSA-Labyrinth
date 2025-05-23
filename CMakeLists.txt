cmake_minimum_required(VERSION 3.10)
project(DSA-Labyrinth)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)

# Add GoogleTest as a subdirectory (optional, if you prefer using GoogleTest directly)
# You can also clone GoogleTest separately if you prefer.
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/googletest")
    add_subdirectory(googletest)
endif()

# Add your source code files
add_executable(stack_test
    languages/cpp/data_structures/stack/stack_list.cpp
    languages/cpp/tests/test_stack.cpp
)
# Link GoogleTest to your tests
target_link_libraries(stack_test
    gtest
    gtest_main
)

# Enable testing
enable_testing()
add_test(
    NAME StackTest
    COMMAND stack_test
)

