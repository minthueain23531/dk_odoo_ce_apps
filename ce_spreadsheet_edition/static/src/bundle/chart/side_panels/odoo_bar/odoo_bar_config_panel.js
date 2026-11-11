import { CommonOdooChartConfigPanel } from "../common/config_panel";
import { components } from "@odoo/o-spreadsheet";

const { Checkbox } = components;

export class OdooBarChartConfigPanel extends CommonOdooChartConfigPanel {
    static template = "ce_spreadsheet_edition.OdooBarChartConfigPanel";

    static components = {
        ...CommonOdooChartConfigPanel.components,
        Checkbox,
    };

    onUpdateStacked(stacked) {
        this.props.updateChart(this.props.chartId, {
            stacked,
        });
    }
}
