python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. cfcalls/protocols/models.proto
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. cfcalls/protocols/signal.proto
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. cfcalls/protocols/events.proto
