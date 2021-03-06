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


#ifndef PROT_SPEC_PEAK_UTIL_HPP_
#define PROT_SPEC_PEAK_UTIL_HPP_

#include "base/mass_constant.hpp"

namespace prot {

namespace peak_util {

inline double compPeakMass(double mono_mz, int charge) {
  return mono_mz * charge - charge * mass_constant::getProtonMass();
}

inline double compMonoMz(double mono_mass, int charge) {
  return mono_mass / charge + mass_constant::getProtonMass();
}

}  // namespace peak_util
}  // namespace prot
#endif
