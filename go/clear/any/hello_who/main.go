// 
// This program or package and any associated files are licensed under the
// Apache License, Version 2.0 (the "License"); you may not use these files
// except in compliance with the License. You can get a copy of the License
// at: http://www.apache.org/licenses/LICENSE-2.0.
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// hello_who
package main 

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	who := "World"
	if len(os.Args) > 1 {
		who = strings.Join(os.Args[1:], " ")
	}
	fmt.Println("hello -> ", who)
}