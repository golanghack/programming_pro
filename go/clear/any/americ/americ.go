// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

var britAmerican = "british-american.txt"

func init() {
	dir, _ := filepath.Split(os.Args[0])
	britAmerican = filepath.Join(dir, britAmerican)
}


func main() {
	inFilename, outFilename, err := filenamesFromCL()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	inFile, outFile := os.Stdin, os.Stdout
	if inFilename != "" {
		if inFile, err = os.Open(inFilename); err != nil {
			log.Fatal(err)
		}
		defer inFile.Close()
	}
	if outFilename != "" {
		if outFile, err = os.Create(outFilename); err != nil {
			log.Fatal(err)
		}
		defer outFile.Close()
	}
	if err = americ(inFile, outFile); err != nil {
		log.Fatal(err)
	}
}


func filenamesFromCL() (inFilename, outFilename string, err error) {
	if len(os.Args) > 1 && (os.Args[1] == "-h" || os.Args[1] == "--help") {
		err = fmt.Errorf("usage -> %s [<]infile.txt [>]outfile.txt", filepath.Base(os.Args[0]))
		return "", "", err
	}
	if len(os.Args) > 1 {
		inFilename = os.Args[1]
		if len(os.Args) > 2 {
			outFilename = os.Args[2]
		}
	}
	if inFilename != "" && inFilename == outFilename {
		log.Fatal("wont overwite the infile")
	}
	return inFilename, outFilename, nil
}

func americ(inFile io.Reader, outFile io.Writer) (err error) {
	reader := bufio.NewReader(inFile)
	writer := bufio.NewWriter(outFile)
	defer func() {
		if err != nil {
			err = writer.Flush()
		}
	}()
	var replacer func(string) string
	if replacer, err = makeReplacerFunction(britAmerican); err != nil {
		return err 
	}
	wordRx := regexp.MustCompile("[A-Za-z]+")
	eof := false
	for !eof {
		var line string
		line, err = reader.ReadString('\n')
		if err == io.EOF {
			err = nil
			eof = true
		} else if err != nil {
			return err 
		}
		line = wordRx.ReplaceAllStringFunc(line, replacer)
		if _, err = writer.WriteString(line); err != nil {
			return err
		}
	}
	return nil 
}

func makeReplacerFunction(file string) (func(string) string, error) {
	rawBytes, err := os.ReadFile(file)
	if err != nil {
		return nil, err 
	}
	text := string(rawBytes)
	
	usForBritish := make(map[string]string)
	lines := strings.Split(text, "\n")
	for _, line := range lines {
		fields := strings.Fields(line)
		if len(fields) == 2 {
			usForBritish[fields[0]] = fields[1]
		}
	}
	return func(word string) string {
		if usWord, found := usForBritish[word]; found {
			return usWord
		}
		return word 
	}, nil 
}