// Compile: 
// $ clang++ --std=c++17 assign.cc

#include <vector>
#include <iostream>

class Solution {
 public:
  Solution(int num_groups) {
    for (int i = 0; i < num_groups; ++i) {
      groups_.push_back({});
    }
  }

  std::vector<std::vector<int>> groups_;
};

int main(void) {
  int num_groups = 5;

  std::vector<Solution> solutions;
  for (int i0 = 0; i0 < num_groups; i0++) {
    for (int i1 = 0; i1 < num_groups; i1++) {
      for (int i2 = 0; i2 < num_groups; i2++) {
        for (int i3 = 0; i3 < num_groups; i3++) {
          for (int i4 = 0; i4 < num_groups; i4++) {
            for (int i5 = 0; i5 < num_groups; i5++) {
              for (int i6 = 0; i6 < num_groups; i6++) {
                for (int i7 = 0; i7 < num_groups; i7++) {
                  for (int i8 = 0; i8 < num_groups; i8++) {
                    for (int i9 = 0; i9 < num_groups; i9++) {
                      solutions.emplace_back(num_groups);
                      solutions.back().groups_[i0].push_back(0);
                      solutions.back().groups_[i1].push_back(1);
                      solutions.back().groups_[i2].push_back(2);
                      solutions.back().groups_[i3].push_back(3);
                      solutions.back().groups_[i4].push_back(4);
                      solutions.back().groups_[i5].push_back(5);
                      solutions.back().groups_[i6].push_back(6);
                      solutions.back().groups_[i7].push_back(7);
                      solutions.back().groups_[i8].push_back(8);
                      solutions.back().groups_[i9].push_back(9);
                      if (solutions.size() % 1000000 == 0) {
                        std::cout << solutions.size() << " solutions are created.\n";
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }

  std::cout << "In total " << solutions.size() << " solutions are created.\n";
}
