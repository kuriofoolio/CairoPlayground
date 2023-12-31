# CairoPlayground: Experimentation with PyCairo

# Getting Started with PyCairo

This guide will help you get started with PyCairo, a Python library for creating 2D vector graphics. PyCairo allows you to create beautiful graphics, illustrations, and charts in your Python applications.

## Prerequisites

Before you begin, make sure you have the following prerequisites:

- Python installed on your system.
- PyCairo library installed. You can install it using pip:

  ```bash
  pip install pycairo


# Using PyCairo

1. Import PyCairo
In your Python script, import the PyCairo library:

```bash 
import cairo
```

2. Create a Cairo Context

```bash
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)
```

3. Drawing Shapes

```bash
context.rectangle(x, y, width, height)
context.set_source_rgb(0.5, 0.5, 1)  # Set the fill color
context.fill()
```

4. Saving the Image

```bash
surface.write_to_png("output.png")
```
