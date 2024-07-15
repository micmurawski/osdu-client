from __future__ import annotations

import re
from collections import defaultdict


class SwaggerDoc(dict):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.segregate_paths()

    @property
    def versions(self):
        return list(self.paths.keys())

    def segregate_paths(self) -> list[str]:
        self.paths = defaultdict(list)

        for path in self["paths"]:
            val = re.search(r"v([0-9]+)", path)
            if val:
                self.paths[val.group()].append(
                    path
                )
            else:
                self.paths["common"].append(
                    path
                )

        if "common" in self.paths and len(self.paths) == 2:
            main_paths = self.paths.pop("common")
            paths = self.paths.pop(list(self.paths.keys())[0])
            self.paths = defaultdict(list)
            self.paths["common"] = main_paths + paths


if __name__ == "__main__":
    # import yaml
    import json
    swagger = SwaggerDoc(
        json.load(
            open("/Users/micmur/GITHUB/osdu-client/osdu_client/services/rafs/swagger.yaml", "r")
        )
    )
    # print(swagger)
    print(swagger.versions)
