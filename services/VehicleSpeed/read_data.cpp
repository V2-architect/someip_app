#include <iostream>
#include <fstream>
#include <vector>

std::vector<float> get_data() {
    std::ifstream inputFile("vehicle_speed.txt");
    
    if (!inputFile.is_open()) {
        std::cerr << "can't open file." << std::endl;
        return NULL;
    }
    
    std::vector<float> floatValues;
    float value;

    while (inputFile >> value) {
        floatValues.push_back(value);
    }

    inputFile.close();

    return floatValues;
}

int main() {
    std::vector<float> floatValues;

    if (floatValues.size() == 3) {
        std::cout << "the values from file: "
                  << floatValues[0] << ", "
                  << floatValues[1] << ", "
                  << floatValues[2] << std::endl;
    } else {
        std::cerr << "no 3 values." << std::endl;
    }

    return 0;
}

