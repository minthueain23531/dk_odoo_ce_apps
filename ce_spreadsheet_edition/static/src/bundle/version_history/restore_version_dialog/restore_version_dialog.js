import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

export class RestoreVersionConfirmationDialog extends ConfirmationDialog {
    static template = "ce_spreadsheet_edition.RestoreVersionConfirmationDialog";
    static props = {
        ...ConfirmationDialog.props,
        makeACopy: { type: Function },
    };

    async _makeACopy() {
        return this.execButton(this.props.makeACopy);
    }
}
