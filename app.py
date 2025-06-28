#!/usr/bin/env python3
import os

import aws_cdk as cdk

from kiritsu.kiritsu_stack import KiritsuStack


app = cdk.App()
KiritsuStack(app, "KiritsuStack")
app.synth()
