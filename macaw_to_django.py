#!/usr/bin/env python

import argparse
from macaw.templates import TemplateUpdater


def main():

    parser = argparse.ArgumentParser(description="macaw_to_django")

    parser.add_argument("definitions",
                        help="The YAML definitions files.")

    parser.add_argument("template_dir",
                        help="The Template base dir")

    parser.add_argument("design_paths",
                        nargs="*",
                        help="Specify the Macaw publish path.")

    args = parser.parse_args()

    updater = TemplateUpdater(args.definitions)

    updater.watch(designbase=args.design_paths[0],
                  templatebase=args.template_dir)


if __name__ == "__main__":
    main()

