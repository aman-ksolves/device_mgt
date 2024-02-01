/** @odoo-module **/
import { _t } from "@web/core/l10n/translation";
import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { useService } from "@web/core/utils/hooks";

export class ExportButton extends ListController {
   setup() {
        super.setup();
        this.orm = useService("orm")
        this.rpc = useService("rpc");
        this.actionService = useService("action");
//            const someString = this.env._t('some text');
//          console.log('hello from setup')
//          const user = useService("user");
//          console.log(user.context);
    }
    async test(){
//      console.log(this.props)
        var selectedResIds = await this.getSelectedResIds();
        if (selectedResIds.length != 0){
             await this.orm.call("device.assignment", "changeState", [selectedResIds])
            .then((data)=>{
                console.log('data',data)

                this.actionService.doAction({
                 type: "ir.actions.client",
                    tag: "soft_reload",

            });
//                return this.rpc('/test')
            })
        }

    }

}



registry.category("views").add("button_in_tree", {
    ...listView,
    Controller: ExportButton,
});


//const serviceRegistry = registry.category("services");
//
//const myService = {
//    dependencies: ["notification"],
//    start(env, { notification }) {
//        let counter = 1;
//        setInterval(() => {
//            notification.add(_t(`Tick Tock ${counter++}`));
//        }, 5000);
//    }
//};
//
//serviceRegistry.add("myService", myService);