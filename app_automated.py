# # File: app.py
# # language: python
# from pathlib import Path
# import importlib
# import sys
# from flask import Flask, request, jsonify
# from typing import Dict
# from rules.base import BaseFlow
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# def load_flows() -> Dict[str, BaseFlow]:
#     """
#     Discover subfolders in `rules/` that contain a `flow.py`.
#     For each, import module and obtain an instance via `get_flow()` or by finding
#     a subclass of BaseFlow.
#     """
#     flows = {}
#     rules_dir = Path(__file__).parent / "rules"
#     if str(Path(__file__).parent) not in sys.path:
#         sys.path.insert(0, str(Path(__file__).parent))
#
#     for entry in rules_dir.iterdir():
#         if not entry.is_dir():
#             continue
#         flow_path = entry / "flow.py"
#         if not flow_path.exists():
#             continue
#         module_name = f"rules.{entry.name}.flow"
#         try:
#             mod = importlib.import_module(module_name)
#         except Exception as exc:
#             app.logger.error("Failed to import %s: %s", module_name, exc)
#             continue
#
#         instance = None
#         if hasattr(mod, "get_flow"):
#             try:
#                 instance = mod.get_flow()
#             except Exception as exc:
#                 app.logger.error("get_flow() in %s failed: %s", module_name, exc)
#                 continue
#         else:
#             # find first concrete subclass of BaseFlow
#             for attr in dir(mod):
#                 obj = getattr(mod, attr)
#                 if isinstance(obj, type) and issubclass(obj, BaseFlow) and obj is not BaseFlow:
#                     try:
#                         instance = obj(entry.name)
#                         break
#                     except Exception as exc:
#                         app.logger.error("Failed to instantiate %s.%s: %s", module_name, attr, exc)
#                         instance = None
#                         break
#
#         if instance:
#             flows[entry.name] = instance
#
#     return flows
#
# def make_view(flow: BaseFlow):
#     def view():
#         try:
#             payload = request.get_json(force=True, silent=True) or {}
#             result = flow.execute(payload)
#             return jsonify(result), 200
#         except Exception as exc:
#             app.logger.exception("Flow %s failed", flow.name)
#             return jsonify({"error": "internal flow error", "details": str(exc)}), 500
#     return view
#
# # Register flows dynamically
# flows = load_flows()
# for name, flow in flows.items():
#     endpoint = f"rules.{name}"
#     route = f"/{name}"
#     app.add_url_rule(route, endpoint, make_view(flow), methods=["POST"])
#
# if __name__ == '__main__':
#     app.run()
