from graphics_processor import pipelines


class GraphicsProcessor(object):
    # simple class which wraps a graphics processing pipeline
    # pipeline objects may get reused across consists,
    # so we don't store consist info in the pipeline, it's passed to pipeline.render() method when needed
    def __init__(self, pipeline_name):
        self.pipeline_name = pipeline_name
        self.pipeline = pipelines.get_pipeline(pipeline_name)