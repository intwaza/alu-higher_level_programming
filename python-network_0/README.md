# Python Network 0 - Bash/cURL Scripts

Bash scripts demonstrating HTTP networking concepts using cURL.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `0-body_size.sh` | Get response body size in bytes | `./0-body_size.sh <URL>` |
| `1-body.sh` | Display body only for 200 status | `./1-body.sh <URL>` |
| `3-methods.sh` | Show accepted HTTP methods | `./3-methods.sh <URL>` |
| `4-header.sh` | Send GET with custom header | `./4-header.sh <URL>` |
| `5-post_params.sh` | Send POST with form data | `./5-post_params.sh <URL>` |

## Setup
```bash
chmod +x *.sh
```

## Examples
```bash
./0-body_size.sh 0.0.0.0:5000              # Output: 10
./1-body.sh 0.0.0.0:5000/route_1           # Output: Route 2
./3-methods.sh 0.0.0.0:5000/route_4        # Output: OPTIONS, HEAD, PUT
./4-header.sh 0.0.0.0:5000/route_5         # Output: Hello Holberton School!
./5-post_params.sh 0.0.0.0:5000/route_6    # Output: POST params: email: test@gmail.com...
```

## Requirements
- Bash shell
- cURL installed
- Test server on port 5000