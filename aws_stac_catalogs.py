import json
import os
import shutil
import yaml
import leafmap
import pandas as pd

url = "https://github.com/awslabs/open-data-registry/archive/refs/heads/main.zip"
out_dir = "open-data-registry-main"
zip_file = "open-data-registry-main.zip"

if os.path.exists(out_dir):
    shutil.rmtree(out_dir)

if os.path.exists(zip_file):
    os.remove(zip_file)

leafmap.download_file(url, output=zip_file, unzip=True)


in_dir = os.path.join(out_dir, "datasets")

files = leafmap.find_files(in_dir, ext=".yaml")

print(f"Total number of AWS open datasets: {len(files)}")

datasets = []
names = {}

for file in files:
    dataset = {}
    with open(file, "r") as f:
        dataset = yaml.safe_load(f)

        if "Deprecated" in dataset:
            continue

        tags = dataset.get("Tags", [])
        name = dataset.get("Name", "")

        if "stac" in tags:

            basename = os.path.basename(file)
            out_file = os.path.join("datasets", basename)

            shutil.copy(file, out_file)

            resources = dataset.get("Resources", [])

            for resource in resources:

                if "Explore" in resource:

                    names[name] = names.get(name, 0) + 1

            for resource in resources:

                if "Explore" in resource:
                    explore = resource["Explore"][0]
                    url = explore[explore.find("http") : -1]

                    resource.pop("Explore")

                    item = {}

                    resource["Description"] = resource["Description"].replace(
                        "Water Observations from Space ", ""
                    )

                    if names[name] > 1:
                        item[
                            "Name"
                        ] = f"{name} - {resource['Description'].replace(name, '')}"
                    else:
                        item["Name"] = name

                    item["Name"] = item["Name"].replace("/", "-").replace("-  -", "-")

                    item["Endpoint"] = url

                    for key in resource:
                        item[key] = resource[key]

                    datasets.append(item)


print(f"Total number of STAC datasets: {len(datasets)}")

df = pd.DataFrame(datasets)
df = df.sort_values(by="Name")
df.to_csv("aws_stac_catalogs.tsv", index=False, sep="\t")

data = json.loads(df.to_json(orient="records"))

with open("aws_stac_catalogs.json", "w") as f:
    json.dump(data, f, indent=4)
