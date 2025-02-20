#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.gui.i18n import _
from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)
from cmk.gui.valuespec import Dictionary, Filesize, Tuple


def _parameter_valuespec_graylog_cluster_traffic():
    return Dictionary(
        elements=[
            (
                "input",
                Tuple(
                    title=_("Absolute levels for input traffic"),
                    elements=[Filesize(title=_("Warning at")), Filesize(title=_("Critical at"))],
                ),
            ),
            (
                "output",
                Tuple(
                    title=_("Absolute levels for output traffic"),
                    elements=[Filesize(title=_("Warning at")), Filesize(title=_("Critical at"))],
                ),
            ),
            (
                "decoded",
                Tuple(
                    title=_("Absolute levels for decoded traffic"),
                    elements=[Filesize(title=_("Warning at")), Filesize(title=_("Critical at"))],
                ),
            ),
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name="graylog_cluster_traffic",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_graylog_cluster_traffic,
        title=lambda: _("Graylog cluster traffic"),
    )
)
