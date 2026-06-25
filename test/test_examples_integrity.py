from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]


def _load_crazy_machines_objects():
    path = ROOT / "classes_first" / "crazy_machines" / "objects.py"
    spec = spec_from_file_location("crazy_machines_objects", path)
    module = module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_all_example_python_files_compile():
    for path in ROOT.rglob("*.py"):
        compile(path.read_text(encoding="utf-8"), path, "exec")


def test_object_factory_ignores_clicks_after_object_limit_is_reached():
    objects = _load_crazy_machines_objects()
    factory = object.__new__(objects.ObjectFactory)
    factory.needs_two_clicks = True
    factory.saved_mouse_pos = None
    factory.selector_label = SimpleNamespace(get_value=lambda: 0)
    factory.world = SimpleNamespace(camera=SimpleNamespace(is_in_screen=lambda position: True))

    factory.on_down((10, 10))

    assert factory.saved_mouse_pos is None


def test_line_factory_respects_object_limit():
    objects = _load_crazy_machines_objects()
    factory = object.__new__(objects.LineFactory)
    factory.saved_mouse_pos = (0, 0)
    factory.max_length = 100
    factory.selector_label = SimpleNamespace(get_value=lambda: 0)
    factory.world = SimpleNamespace(distance_to=lambda first, second: 20)

    assert not factory.valid_placement((10, 10))
