//Copyright (c) 2014 - 2018, The Trustees of Indiana University.
//
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.


#ifndef PROT_FEATURE_CHARGE_CMP_HPP_
#define PROT_FEATURE_CHARGE_CMP_HPP_

#include <memory>
#include <vector>

#include "spec/peak.hpp"
#include "feature/match_env.hpp"

namespace prot {

class ChargeCmp {
 public:
  static int comp(PeakPtrVec &peak_list, MatchEnvPtr a, MatchEnvPtr b, double tolerance);
};

}

#endif
