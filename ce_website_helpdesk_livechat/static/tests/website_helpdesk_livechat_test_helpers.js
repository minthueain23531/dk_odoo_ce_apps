import { helpdeskModels } from "@ce_helpdesk/../tests/helpdesk_test_helpers";

import { mailModels } from "@mail/../tests/mail_test_helpers";

import { ResUsers } from "@ce_website_helpdesk_livechat/../tests/mock_server/models/res_users";
import { websiteLivechatModels } from "@website_livechat/../tests/website_livechat_test_helpers";

import { defineModels } from "@web/../tests/web_test_helpers";

export const websiteHelpdeskLivechatModels = {
    ...helpdeskModels,
    ...mailModels,
    ...websiteLivechatModels,
    ResUsers,
};

export function defineWebsiteHelpdeskLivechatModels() {
    return defineModels(websiteHelpdeskLivechatModels);
}
