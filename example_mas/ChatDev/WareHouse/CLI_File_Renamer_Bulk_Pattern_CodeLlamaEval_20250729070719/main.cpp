#include <iostream>
#include <string>
#include <filesystem>
int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <pattern> <directory>" << std::endl;
        return 1;
    }
    std::string pattern = argv[1];
    std::string directory = argv[2];
    for (const auto &entry : std::filesystem::directory_iterator(directory)) {
        std::string filename = entry.path().filename().string();
        std::string new_filename = rename_file(filename, pattern);
        if (!new_filename.empty()) {
            std::filesystem::rename(entry.path(), directory + "/" + new_filename);
        }
    }
    return 0;
}
std::string rename_file(std::string filename, std::string pattern) {
    // Implement rename logic here
    return filename;
}