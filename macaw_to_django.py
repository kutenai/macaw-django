#!/usr/bin/env python

import argparse
from macaw.templates import TemplateUpdater


def main():

    parser = argparse.ArgumentParser(description="macaw_to_django")

    parser.add_argument("definitions",
                        help="The YAML definitions files.")

    parser.add_argument("tempate_dir",
                        help="The Template base dir")

    parser.add_argument("design_paths",
                        nargs="*",
                        help="Specify the Macaw publish path.")

    args = parser.parse_args()

    updater = TemplateUpdater(args.definitions, args.design_paths)

    updater.watch(args.design_paths[0])


if __name__ == "__main__":
    main()

