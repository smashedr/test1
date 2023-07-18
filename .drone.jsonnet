local Pipeline(name, image) = {
  kind: "pipeline",
  name: name,
  steps: [
    {
      name: "test",
      image: image,
      commands: [
        "python -V"
        "python myapp.py"
      ]
    }
  ]
};

[
  Pipeline("python-3-8", "python:3.8"),
  Pipeline("python-3-9", "python:3.9"),
]
