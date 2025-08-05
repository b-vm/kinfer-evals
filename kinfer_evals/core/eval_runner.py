"""CLI driver:  kinfer-eval  <policy>  <robot>  <eval-name>  [--seconds] [--out]"""

import argparse, asyncio
import colorlogging                # NEW

from pathlib import Path

from kinfer_evals.evals import REGISTRY
from kinfer_evals.core.types import RunArgs
from kinfer_evals.core.eval_engine import run_eval

_p = argparse.ArgumentParser(prog="kinfer-eval")
_p.add_argument("kinfer", type=Path)
_p.add_argument("robot")
_p.add_argument("eval", choices=sorted(REGISTRY.keys()))
_p.add_argument("--out", type=Path, default=Path("runs"))
_p.add_argument("--seconds", type=float, default=5.0)

def main() -> None:
    colorlogging.configure(level="INFO")    # NEW – pretty, coloured output

    ns   = _p.parse_args()
    make = REGISTRY[ns.eval]          # the registered function
    args = RunArgs(ns.eval, ns.kinfer, ns.robot, ns.out, ns.seconds)
    asyncio.run(run_eval(make, ns.eval, args))

if __name__ == "__main__":
    main()
