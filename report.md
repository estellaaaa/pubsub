# Report 1

Estella Kinzel, Tobias Bayer

## Responsibilities

### Estella

Implement server and client with build-in `socket`.

### Tobias

Implement a basic rpc module with build-in `json`.

## Brief explanation

### Scenario

In our simple rpc system, we use two terminals on the same machine to call a remote procedure via localhost. We run the server module in one terminal and, in another terminal, run python in interactive mode. In interactive mode, we import our client module to get access to it's stub function. We call the function and observe the behavior. The first terminal (server) shows some log output with information about the caller. The client terminal shows the server's response, which matches what we have expected.

### Programming language

We use python 3.11 and have no other dependencies.

### Sources

* <https://alexanderell.is/posts/rpc-from-scratch/>
* <https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python>
* <https://www.computerweekly.com/de/definition/Remote-Procedure-Call-RPC>

