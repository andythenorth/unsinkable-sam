from graphics_processor import pipelines


class GraphicsProcessor(object):
    # simple class which wraps a graphics processing pipeline along with some options
    # pipeline objects may get reused across consists,
    # so we don't store consist info in the pipeline, it's passed to pipeline.render() method when needed
    def __init__(self, pipeline_name, options):
        self.pipeline_name = pipeline_name
        self.options = options
        self.pipeline = pipelines.get_pipeline(pipeline_name)


def get_composited_cargo_processors(template):
    # returns a cargo-compositing graphics processors
    options = {'template': template}
    graphics_processor = GraphicsProcessor('extend_spriterows_for_composited_cargos_pipeline', options)
    return [graphics_processor]
