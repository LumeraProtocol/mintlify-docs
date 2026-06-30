# Source: https://github.com/LumeraProtocol/rq-go

### Uh oh!

There was an error while loading. [Please reload this page]().

[LumeraProtocol](https://github.com/LumeraProtocol) / **[rq-go](https://github.com/LumeraProtocol/rq-go)** Public

- [Notifications](https://github.com/login?return_to=%2FLumeraProtocol%2Frq-go) You must be signed in to change notification settings
- [Fork 1](https://github.com/login?return_to=%2FLumeraProtocol%2Frq-go)
- [Star 3](https://github.com/login?return_to=%2FLumeraProtocol%2Frq-go)
 

 

 main

[Branches](https://github.com/LumeraProtocol/rq-go/branches) [Tags](https://github.com/LumeraProtocol/rq-go/tags)

Go to file

Code

Open more actions menu

## Folders and files

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

## Latest commit

## History

[9 Commits](https://github.com/LumeraProtocol/rq-go/commits/main/)

9 Commits

 |
| 

[include](https://github.com/LumeraProtocol/rq-go/tree/main/include 'include')

 | 

[include](https://github.com/LumeraProtocol/rq-go/tree/main/include 'include')

 | 

 | 

 |
| 

[lib](https://github.com/LumeraProtocol/rq-go/tree/main/lib 'lib')

 | 

[lib](https://github.com/LumeraProtocol/rq-go/tree/main/lib 'lib')

 | 

 | 

 |
| 

[test-client](https://github.com/LumeraProtocol/rq-go/tree/main/test-client 'test-client')

 | 

[test-client](https://github.com/LumeraProtocol/rq-go/tree/main/test-client 'test-client')

 | 

 | 

 |
| 

[.gitignore](https://github.com/LumeraProtocol/rq-go/blob/main/.gitignore '.gitignore')

 | 

[.gitignore](https://github.com/LumeraProtocol/rq-go/blob/main/.gitignore '.gitignore')

 | 

 | 

 |
| 

[LICENSE](https://github.com/LumeraProtocol/rq-go/blob/main/LICENSE 'LICENSE')

 | 

[LICENSE](https://github.com/LumeraProtocol/rq-go/blob/main/LICENSE 'LICENSE')

 | 

 | 

 |
| 

[README.md](https://github.com/LumeraProtocol/rq-go/blob/main/README.md 'README.md')

 | 

[README.md](https://github.com/LumeraProtocol/rq-go/blob/main/README.md 'README.md')

 | 

 | 

 |
| 

[go.mod](https://github.com/LumeraProtocol/rq-go/blob/main/go.mod 'go.mod')

 | 

[go.mod](https://github.com/LumeraProtocol/rq-go/blob/main/go.mod 'go.mod')

 | 

 | 

 |
| 

[raptorq.go](https://github.com/LumeraProtocol/rq-go/blob/main/raptorq.go 'raptorq.go')

 | 

[raptorq.go](https://github.com/LumeraProtocol/rq-go/blob/main/raptorq.go 'raptorq.go')

 | 

 | 

 |
| 

[raptorq\_test.go](https://github.com/LumeraProtocol/rq-go/blob/main/raptorq_test.go 'raptorq_test.go')

 | 

[raptorq\_test.go](https://github.com/LumeraProtocol/rq-go/blob/main/raptorq_test.go 'raptorq_test.go')

 | 

 | 

 |
| 

View all files

 |

## Repository files navigation

# RaptorQ Go Bindings

This repository contains Go bindings for the RaptorQ erasure coding library. RaptorQ is a Forward Error Correction (FEC) code that allows for efficient recovery of data from partial information. This package enables encoding files into RaptorQ symbols and decoding them back, providing resilience against data loss.

## Key Features

- **Memory-Efficient Block Processing**: Files are split into blocks for processing, with each block encoded separately to minimize memory usage
- **Built-in Resource Management**: Explicit control over memory usage and concurrency limits
- **Flexible Configuration**: Customizable symbol size, redundancy factor, and other parameters
- **Error Recovery**: Can recover the original file even if some symbols are missing
- **Cross-Platform Support**: Works on multiple platforms including Linux, macOS, and Windows
- **Static Linking**: Library is statically linked, making the final binary self-contained

## Repository Structure

```
rq-go/
├── README.md                 # This file
├── go.mod                    # Root Go module file
├── raptorq.go                # Main Go binding code
├── raptorq_test.go           # Tests for the Go bindings
└── lib/                      # Platform-specific libraries
    ├── README.md             # Documentation for the libraries
    ├── darwin/               # macOS libraries
    │   ├── amd64/            # Intel macOS
    │   │   └── librq_library.a
    │   └── arm64/            # Apple Silicon
    │       └── librq_library.a
    ├── linux/                # Linux libraries
    │   ├── amd64/            # amd64
    │   │   └── librq_library.a
    │   └── arm64/            # ARM64
    │       └── librq_library.a
    └── windows/              # Windows libraries
        └── amd64/            # amd64
            └── librq_library.a
```

## Platform Support

The platform subfolder structure follows Go's standard naming convention:

- `darwin/amd64` - macOS on Intel
- `darwin/arm64` - macOS on Apple Silicon
- `linux/amd64` - Linux on amd64
- `linux/arm64` - Linux on ARM64 (including Raspberry Pi)
- `windows/amd64` - Windows on amd64

## Installation

To use this package in your Go project:

```shell
go get github.com/LumeraProtocol/rq-go
```

Then import it in your code:

```go
import "github.com/LumeraProtocol/rq-go"
```

## Usage

### Creating a Processor

```go
package main

import (
    "log"
    "github.com/LumeraProtocol/rq-go"
)

func main() {
    // Create a processor with default settings
    processor, err := raptorq.NewDefaultRaptorQProcessor()
    if err != nil {
        log.Fatalf("Failed to create processor: %v", err)
    }
    defer processor.Free() // Always free the processor when done

    // Or create with custom settings
    customProcessor, err := raptorq.NewRaptorQProcessor(
        65535,           // Symbol size (bytes)
        4,               // Redundancy factor
        4 * 1024,        // Max memory (MB) - 4GB
        2,               // Concurrency limit
    )
    // Use customProcessor...
}
```

### Encoding a File

```go
package main

import (
    "fmt"
    "log"
    "os"
    "github.com/LumeraProtocol/rq-go"
)

func encodeExample() {
    processor, err := raptorq.NewDefaultRaptorQProcessor()
    if err != nil {
        log.Fatalf("Failed to create processor: %v", err)
    }
    defer processor.Free()

    // Get recommended block size for memory-efficient processing
    fileInfo, err := os.Stat("large_file.dat")
    if err != nil {
        log.Fatalf("Failed to get file info: %v", err)
    }
    blockSize := processor.GetRecommendedBlockSize(uint64(fileInfo.Size()))

    // Encode the file using the recommended block size
    result, err := processor.EncodeFile("large_file.dat", "symbols/", blockSize)
    if err != nil {
        log.Fatalf("Encoding failed: %v", err)
    }

    fmt.Printf("Encoded file with %d total symbols\n", result.TotalSymbolsCount)
    fmt.Printf("Layout file created at: %s\n", result.LayoutFilePath)
}
```

### Decoding Symbols

```go
package main

import (
    "fmt"
    "log"
    "github.com/LumeraProtocol/rq-go"
)

func decodeExample() {
    processor, err := raptorq.NewDefaultRaptorQProcessor()
    if err != nil {
        log.Fatalf("Failed to create processor: %v", err)
    }
    defer processor.Free()

    // Decode symbols back to the original file
    err = processor.DecodeSymbols("symbols/", "recovered.dat", "symbols/_raptorq_layout.json")
    if err != nil {
        log.Fatalf("Decoding failed: %v", err)
    }

    fmt.Println("File successfully recovered")
}
```

### Creating Metadata Only

```go
package main

import (
    "fmt"
    "log"
    "github.com/LumeraProtocol/rq-go"
)

func metadataExample() {
    processor, err := raptorq.NewDefaultRaptorQProcessor()
    if err != nil {
        log.Fatalf("Failed to create processor: %v", err)
    }
    defer processor.Free()

    // Generate metadata without creating symbols (for planning purposes)
    result, err := processor.CreateMetadata("large_file.dat", "layout.json", 1024*1024)
    if err != nil {
        log.Fatalf("Metadata creation failed: %v", err)
    }

    fmt.Printf("File would be encoded with %d total symbols\n", result.TotalSymbolsCount)
}
```

## Block Processing and Memory Management

The RaptorQ library processes files in blocks to efficiently manage memory usage:

1. Files are split into blocks of a specified size
2. Each block is processed separately, minimizing peak memory usage
3. The `GetRecommendedBlockSize` function calculates an optimal block size based on:
 - File size
 - Available memory (configured via `maxMemoryMB`)
 - Processing efficiency
 - Recovery capabilities

For large files, using the recommended block size is crucial to avoid excessive memory consumption.

## Metadata File Format

During encoding, the library creates a metadata file (`_raptorq_layout.json`) in the output directory. This file contains:

- Encoder parameters
- Block information (size, offset, etc.)
- Symbol identifiers

This metadata is essential for the decoding process, especially when files are split into multiple blocks.

```json
{
  "blocks": [
    { 
      "block_id": integer, // block ID,
      "encoder_parameters": [/* 12 bytes */], // encoder parameters,
      "original_offset": integer, // offset of the block in the original file,
      "size": integer, // size of the block,
      "symbols": ["string", ...], // array of symbol hashes
      "hash": "block hash"  // hash of the block
    },
    ...
  ],
}
```

If input file is not split into blocks, the metadata file will contain only one block with ID 0.

### Example Metadata File

```json
{
  "blocks": [
    {
      "block_id": 0,
      "encoder_parameters": [
        0,
        0,
        25,
        240,
        160,
        0,
        195,
        80,
        1,
        0,
        1,
        8
      ],
      "original_offset": 0,
      "size": 1700000,
      "symbols": [
        "9yCaAXSexMsaWDP6pzK4wZ4w9Hqrr6QPjJZ86wJMGoq9",
        "3Q4MtczkeZzWbECcA8eUeMaQ14cGHF4PpgeYo33cMtYD",
        "G6okoLMA1wGtVZwieSykR9bvLSw49iwYZux2byJDrbDF",
        "AJ9fp8Ydqo1aaVHzjHowajJA4ELwfetpQAMUT47GZays"
      ],
      "hash": "9gD64LFuoQPYJoWBQmnG2TdPErWwni7Bhrpn6ae74rk7"
    },
    {
      "block_id": 1,
      "encoder_parameters": [
        0,
        0,
        25,
        240,
        160,
        0,
        195,
        80,
        1,
        0,
        1,
        8
      ],
      "original_offset": 1700000,
      "size": 1700000,
      "symbols": [
        "CxFNCbQhtWLzXwpGCE8L1m67WEV85zuTpTtYyRm6nDQF",
        "8NVZfQzFDsXwQgEbuNxzyo9D18da9qEHfDpou7mCzg72",
        "2hsAk5xWZCJ6d3xnnEaPu6TXsVwN6vfVhLDbKo7fsGVd",
        "96KaGntmMeqzL9uPxpKce2PMV9BiUXovMiDUBw1t3Mhz",
        "3kMQUazSrgfpxxkw3yY9zfh8amHXCeD7ZsmaDCu2szdB"
      ],
      "hash": "9LvSmppDKePbZnY6PLX8hyEY8gcskVJKwzmgn7zyPNyC"
    }
  ]
}
```

## Configuration Options

The RaptorQ processor can be configured with several parameters:

| Parameter | Description | Default |
| --- | --- | --- |
| `symbolSize` | Size of each symbol in bytes | 65535 (64KB - 1 byte) |
| `redundancyFactor` | Number of repair symbols per source symbol | 4 |
| `maxMemoryMB` | Maximum memory usage limit in MB | 16384 (16GB) |
| `concurrencyLimit` | Maximum number of concurrent operations | 4 |

## License

This project is licensed under MIT License. See the [LICENSE](https://github.com/LumeraProtocol/rq-go/blob/main/LICENSE) file for details.

## About

No description, website, or topics provided.

### Resources

[Readme](https://github.com/#readme-ov-file)

### License

[MIT license](https://github.com/#MIT-1-ov-file)

### Uh oh!

There was an error while loading. [Please reload this page]().

[Activity](https://github.com/LumeraProtocol/rq-go/activity)

[Custom properties](https://github.com/LumeraProtocol/rq-go/custom-properties)

### Stars

[**3** stars](https://github.com/LumeraProtocol/rq-go/stargazers)

### Watchers

[**1** watching](https://github.com/LumeraProtocol/rq-go/watchers)

### Forks

[**1** fork](https://github.com/LumeraProtocol/rq-go/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FLumeraProtocol%2Frq-go&report=LumeraProtocol+%28user%29)

## [Releases 3](https://github.com/LumeraProtocol/rq-go/releases)

[Version 0.2.1 Latest\\ \\ Apr 24, 2025](https://github.com/LumeraProtocol/rq-go/releases/tag/v0.2.1)

[\+ 2 releases](https://github.com/LumeraProtocol/rq-go/releases)

## [Packages 0](https://github.com/orgs/LumeraProtocol/packages?repo_name=rq-go)

### Uh oh!

There was an error while loading. [Please reload this page]().

### Uh oh!

There was an error while loading. [Please reload this page]().

## [Contributors](https://github.com/LumeraProtocol/rq-go/graphs/contributors)

### Uh oh!

There was an error while loading. [Please reload this page]().

## Languages

- [Go 92.6%](https://github.com/LumeraProtocol/rq-go/search?l=go)
- [C++ 7.4%](https://github.com/LumeraProtocol/rq-go/search?l=c%2B%2B)