# Claude

## Memory

* Memory location : ~/.claude/projects/<project>/memory/
* activated by default
* Claude feed this file
* /memory to browse and read the content of the available files.


## Configuration 

* thinking_budget must be lower than max_tokens or there will be a validation error when calling API (400 Bad Request)
* Some claude options : 
  * claude config
  * claude status
  * claude help
* anthropic-beta header to use beta features


# MCP

* you cannot group MCP servers.
* add tool :  Usage : server.tools(). Parameters : name, description, input_schema (with Zod)

* MCP definition
  * local : ~/.claude.json
  * project : .mcp.json at the root of project folder
 

# Models

 * Claude Sonnet : 8 192 tokens max

# Caching

* if multiple cached prefixes, longest is chosen

# Tools

* message from a tool execution must be returned with the role user
