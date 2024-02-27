import torch

print("Torch version:",torch.__version__)

if (torch.cuda.is_available()):
    print(f"cuda avaiable: {torch.cuda.device_count()}")
else:
    print(f"cuda not avaiable")
