import os

def create_yaml(path, resource):
    yaml = f"apiVersion: kustomize.config.k8s.io/v1beta1\nkind: Kustomization\nnamePrefix: {path.split('/')[-1].replace('layer', '')}-\n\nresources: \n" + resource
    open(f"{path}/kustomization.yaml", "w").write(yaml)

def burst(path: str, n: int):
    if n == 0:
        os.system(f"cp dep.yaml {path}")
        create_yaml(path, "- dep.yaml")
        return

    for j in "abcdefghij":
        os.makedirs(f"{path}/layer{n}{j}")
        burst(f"{path}/layer{n}{j}", n-1)

    create_yaml(path, "\n".join([f"- layer{n}{i}" for i in "abcdefghij"]))

os.mkdir("layer10")
burst("layer10", 9)