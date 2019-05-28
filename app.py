#!/usr/bin/env python3

from aws_cdk import cdk

from queue_viewer.queue_viewer_stack import QueueViewerStack


app = cdk.App()
QueueViewerStack(app, "queue-viewer-cdk-1")

app.run()
