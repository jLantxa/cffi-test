CXX_FLAGS += \
	-std=c++20 \
	-Wall -Werror \
	-Wpedantic -Wconversion

SOURCES += \
	klass.cpp \
	klass_wrapper.cpp

TARGET := libklass.so

all:
	$(CXX) $(CXX_FLAGS) -fPIC -shared $(SOURCES) -o $(TARGET)
