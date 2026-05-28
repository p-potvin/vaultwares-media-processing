import os
import sys
# Find where streamdiffusion is installed
for p in sys.path:
    target = os.path.join(p, 'streamdiffusion', 'tools', 'install-tensorrt.py')
    if os.path.exists(target):
        with open(target, 'r') as f:
            code = f.read()
        code = code.replace('def install(cu: Optional[Literal["11", "12"]] = get_cuda_version_from_torch()):', 'def install(cu: str = "12"):')
        with open(target, 'w') as f:
            f.write(code)
        print("Patched install-tensorrt.py at", target)
        sys.exit(0)
print("Not found")
