// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

console.log(dataObject);
let puppyButton = document.querySelector(`#puppyButton`)
let puppyURL;
let puppyPicture;
puppyButton.addEventListener(`click`,() => {
  console.log(`puperino`)
  puppyURL = dataObject.data["0"].images.original.url;
  console.log(puppyURL);
  puppyPicture = document.createElement(`img`);
  puppyPicture.src = puppyURL;
  document.body.appendChild(puppyPicture);
  console.log(puppyPicture)
})
