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


#include <utility>
#include <string>

#include "base/string_util.hpp"
#include "prsmview/anno_ptm.hpp"

namespace prot {

AnnoPtm::AnnoPtm(PtmPtr ptm_ptr, MassShiftTypePtr type_ptr) {
  ptm_ptr_ = ptm_ptr;
  type_ptr_ = type_ptr;
}

void AnnoPtm::addOccurence(int pos, const std::string &acid_letter) {
  std::pair<int, std::string> new_occurence(pos, acid_letter);
  occurences_.push_back(new_occurence);
}

void AnnoPtm::appendXml(XmlDOMDocument* xml_doc, xercesc::DOMElement* parent) {
  xercesc::DOMElement* element = xml_doc->createElement("expected_change");
  std::string str = type_ptr_->getName();
  xml_doc->addElement(element, "change_type", str.c_str());
  ptm_ptr_->appendAbbrNameToXml(xml_doc, element);

  for (size_t i = 0; i < occurences_.size(); i++) {
    xercesc::DOMElement* position_element = xml_doc->createElement("occurence");
    std::string str = string_util::convertToString(occurences_[i].first);
    xml_doc->addElement(position_element, "position", str.c_str());
    xml_doc->addElement(position_element, "acid_letter", occurences_[i].second.c_str());
    element->appendChild(position_element);
  }
  parent->appendChild(element);
}

AnnoPtmPtr AnnoPtm::findPtm(const AnnoPtmPtrVec &ptm_ptrs, PtmPtr ptm_ptr,
                            MassShiftTypePtr type_ptr) {
  for (size_t i = 0; i < ptm_ptrs.size(); i++) {
    if ((ptm_ptrs[i]->getTypePtr() == type_ptr) &&
        (ptm_ptrs[i]->getPtmPtr() == ptm_ptr)) {
      return ptm_ptrs[i];
    }
  }
  return nullptr;
}

}  // namespace prot
