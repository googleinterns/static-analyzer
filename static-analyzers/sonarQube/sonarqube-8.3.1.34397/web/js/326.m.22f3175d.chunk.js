(window.webpackJsonp=window.webpackJsonp||[]).push([[326],{1905:function(e,t,n){"use strict";n.r(t),n.d(t,"default",(function(){return E}));var r=n(2),a=n(328),o=n(316),i=n.n(o),l=n(5),s=n(878),c=n(310),u=n(334),m=n.n(u);class p extends r.PureComponent{constructor(){super(...arguments),this.state={name:"",url:""},this.handleSubmit=()=>this.props.onSubmit(this.state.name,this.state.url).then(this.props.onClose),this.handleNameChange=e=>{this.setState({name:e.currentTarget.value})},this.handleUrlChange=e=>{this.setState({url:e.currentTarget.value})}}render(){const e=Object(l.translate)("project_links.create_new_project_link");return r.createElement(m.a,{header:e,onClose:this.props.onClose,onSubmit:this.handleSubmit,size:"small"},({onCloseClick:t,onFormSubmit:n,submitting:a})=>r.createElement("form",{onSubmit:n},r.createElement("header",{className:"modal-head"},r.createElement("h2",null,e)),r.createElement("div",{className:"modal-body"},r.createElement("div",{className:"modal-field"},r.createElement("label",{htmlFor:"create-link-name"},Object(l.translate)("project_links.name"),r.createElement("em",{className:"mandatory"},"*")),r.createElement("input",{autoFocus:!0,id:"create-link-name",maxLength:128,name:"name",onChange:this.handleNameChange,required:!0,type:"text",value:this.state.name})),r.createElement("div",{className:"modal-field"},r.createElement("label",{htmlFor:"create-link-url"},Object(l.translate)("project_links.url"),r.createElement("em",{className:"mandatory"},"*")),r.createElement("input",{id:"create-link-url",maxLength:128,name:"url",onChange:this.handleUrlChange,required:!0,type:"text",value:this.state.url}))),r.createElement("footer",{className:"modal-foot"},r.createElement(i.a,{className:"spacer-right",loading:a}),r.createElement(c.SubmitButton,{disabled:a,id:"create-link-confirm"},Object(l.translate)("create")),r.createElement(c.ResetButtonLink,{disabled:a,onClick:t},Object(l.translate)("cancel")))))}}class d extends r.PureComponent{constructor(){super(...arguments),this.mounted=!1,this.state={creationModal:!1},this.handleCreateClick=()=>{this.setState({creationModal:!0})},this.handleCreationModalClose=()=>{this.mounted&&this.setState({creationModal:!1})}}componentDidMount(){this.mounted=!0}componentWillUnmount(){this.mounted=!1}render(){return r.createElement(r.Fragment,null,r.createElement("header",{className:"page-header"},r.createElement("h1",{className:"page-title"},Object(l.translate)("project_links.page")),r.createElement("div",{className:"page-actions"},r.createElement(c.Button,{id:"create-project-link",onClick:this.handleCreateClick},Object(l.translate)("create"))),r.createElement("div",{className:"page-description"},Object(l.translate)("project_links.page.description"))),this.state.creationModal&&r.createElement(p,{onClose:this.handleCreationModalClose,onSubmit:this.props.onCreate}))}}var h=n(587),f=n(373),b=n.n(f),v=n(709),y=n.n(v),_=n(714);class O extends r.PureComponent{constructor(){super(...arguments),this.renderNameForProvided=e=>r.createElement("div",{className:"display-inline-block text-top"},r.createElement("div",null,r.createElement("span",{className:"js-name"},Object(h.a)(e))),r.createElement("div",{className:"note little-spacer-top"},r.createElement("span",{className:"js-type"},"sonar.links.".concat(e.type)))),this.renderName=e=>r.createElement("div",null,r.createElement(y.a,{className:"little-spacer-right",type:e.type}),Object(h.b)(e)?this.renderNameForProvided(e):r.createElement("div",{className:"display-inline-block text-top"},r.createElement("span",{className:"js-name"},e.name))),this.renderDeleteButton=e=>Object(h.b)(e)?null:r.createElement(b.a,{confirmButtonText:Object(l.translate)("delete"),confirmData:e.id,isDestructive:!0,modalBody:Object(l.translateWithParameters)("project_links.are_you_sure_to_delete_x_link",e.name),modalHeader:Object(l.translate)("project_links.delete_project_link"),onConfirm:this.props.onDelete},({onClick:e})=>r.createElement(c.Button,{className:"button-red js-delete-button",onClick:e},Object(l.translate)("delete")))}render(){const{link:e}=this.props;return r.createElement("tr",{"data-name":e.name},r.createElement("td",{className:"nowrap"},this.renderName(e)),r.createElement("td",{className:"nowrap js-url"},Object(_.a)(e.url)?r.createElement("a",{href:e.url,rel:"nofollow noreferrer noopener",target:"_blank"},e.url):e.url),r.createElement("td",{className:"thin nowrap"},this.renderDeleteButton(e)))}}class j extends r.PureComponent{renderHeader(){return r.createElement("thead",null,r.createElement("tr",null,r.createElement("th",{className:"nowrap"},Object(l.translate)("project_links.name")),r.createElement("th",{className:"nowrap width-100"},Object(l.translate)("project_links.url")),r.createElement("th",{className:"thin"}," ")))}render(){if(!this.props.links.length)return r.createElement("div",{className:"note"},Object(l.translate)("no_results"));const e=Object(h.c)(this.props.links).map(e=>r.createElement(O,{key:e.id,link:e,onDelete:this.props.onDelete}));return r.createElement("div",{className:"boxed-group boxed-group-inner"},r.createElement("table",{className:"data zebra",id:"project-links"},this.renderHeader(),r.createElement("tbody",null,e)))}}class E extends r.PureComponent{constructor(){super(...arguments),this.mounted=!1,this.state={loading:!0},this.fetchLinks=()=>{this.setState({loading:!0}),Object(s.c)(this.props.component.key).then(e=>{this.mounted&&this.setState({links:e,loading:!1})},()=>{this.mounted&&this.setState({loading:!1})})},this.handleCreateLink=(e,t)=>Object(s.a)({name:e,projectKey:this.props.component.key,url:t}).then(e=>{this.mounted&&this.setState(({links:t=[]})=>({links:[...t,e]}))}),this.handleDeleteLink=e=>Object(s.b)(e).then(()=>{this.mounted&&this.setState(({links:t=[]})=>({links:t.filter(t=>t.id!==e)}))})}componentDidMount(){this.mounted=!0,this.fetchLinks()}componentDidUpdate(e){e.component.key!==this.props.component.key&&this.fetchLinks()}componentWillUnmount(){this.mounted=!1}render(){return r.createElement("div",{className:"page page-limited"},r.createElement(a.a,{defer:!1,title:Object(l.translate)("project_links.page")}),r.createElement(d,{onCreate:this.handleCreateLink}),r.createElement(i.a,{loading:this.state.loading},this.state.links&&r.createElement(j,{links:this.state.links,onDelete:this.handleDeleteLink})))}}},334:function(e,t,n){"use strict";var r,a=this&&this.__extends||(r=function(e,t){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)t.hasOwnProperty(n)&&(e[n]=t[n])})(e,t)},function(e,t){function n(){this.constructor=e}r(e,t),e.prototype=null===t?Object.create(t):(n.prototype=t.prototype,new n)}),o=this&&this.__assign||function(){return(o=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var a in t=arguments[n])Object.prototype.hasOwnProperty.call(t,a)&&(e[a]=t[a]);return e}).apply(this,arguments)},i=this&&this.__rest||function(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var a=0;for(r=Object.getOwnPropertySymbols(e);a<r.length;a++)t.indexOf(r[a])<0&&Object.prototype.propertyIsEnumerable.call(e,r[a])&&(n[r[a]]=e[r[a]])}return n};Object.defineProperty(t,"__esModule",{value:!0});var l=n(2),s=n(327),c=function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.mounted=!1,t.state={submitting:!1},t.stopSubmitting=function(){t.mounted&&t.setState({submitting:!1})},t.handleCloseClick=function(e){e&&(e.preventDefault(),e.currentTarget.blur()),t.props.onClose()},t.handleFormSubmit=function(e){e.preventDefault(),t.submit()},t.handleSubmitClick=function(e){e&&(e.preventDefault(),e.currentTarget.blur()),t.submit()},t.submit=function(){var e=t.props.onSubmit();e&&(t.setState({submitting:!0}),e.then(t.stopSubmitting,t.stopSubmitting))},t}return a(t,e),t.prototype.componentDidMount=function(){this.mounted=!0},t.prototype.componentWillUnmount=function(){this.mounted=!1},t.prototype.render=function(){var e=this.props,t=e.children,n=e.header,r=e.onClose,a=(e.onSubmit,i(e,["children","header","onClose","onSubmit"]));return l.createElement(s.default,o({contentLabel:n,onRequestClose:r},a),t({onCloseClick:this.handleCloseClick,onFormSubmit:this.handleFormSubmit,onSubmitClick:this.handleSubmitClick,submitting:this.state.submitting}))},t}(l.Component);t.default=c},344:function(e,t,n){"use strict";var r,a=this&&this.__extends||(r=function(e,t){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)t.hasOwnProperty(n)&&(e[n]=t[n])})(e,t)},function(e,t){function n(){this.constructor=e}r(e,t),e.prototype=null===t?Object.create(t):(n.prototype=t.prototype,new n)}),o=this&&this.__assign||function(){return(o=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var a in t=arguments[n])Object.prototype.hasOwnProperty.call(t,a)&&(e[a]=t[a]);return e}).apply(this,arguments)};Object.defineProperty(t,"__esModule",{value:!0});var i=n(2),l=n(5),s=n(316),c=n(310),u=n(425),m=n(334),p=function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.mounted=!1,t.handleSubmit=function(){var e=t.props.onConfirm(t.props.confirmData);return e?e.then(t.props.onClose,(function(){})):void t.props.onClose()},t.renderModalContent=function(e){var n=e.onCloseClick,r=e.onFormSubmit,a=e.submitting,o=t.props,m=o.children,p=o.confirmButtonText,d=o.confirmDisable,h=o.header,f=o.headerDescription,b=o.isDestructive,v=o.cancelButtonText,y=void 0===v?l.translate("cancel"):v;return i.createElement(u.default,null,i.createElement("form",{onSubmit:r},i.createElement("header",{className:"modal-head"},i.createElement("h2",null,h),f),i.createElement("div",{className:"modal-body"},m),i.createElement("footer",{className:"modal-foot"},i.createElement(s.default,{className:"spacer-right",loading:a}),i.createElement(c.SubmitButton,{autoFocus:!0,className:b?"button-red":void 0,disabled:a||d},p),i.createElement(c.ResetButtonLink,{disabled:a,onClick:n},y))))},t}return a(t,e),t.prototype.componentDidMount=function(){this.mounted=!0},t.prototype.componentWillUnmount=function(){this.mounted=!1},t.prototype.render=function(){var e=this.props,t={header:e.header,onClose:e.onClose,noBackdrop:e.noBackdrop,size:e.size};return i.createElement(m.default,o({onSubmit:this.handleSubmit},t),this.renderModalContent)},t}(i.PureComponent);t.default=p},373:function(e,t,n){"use strict";var r,a=this&&this.__extends||(r=function(e,t){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)t.hasOwnProperty(n)&&(e[n]=t[n])})(e,t)},function(e,t){function n(){this.constructor=e}r(e,t),e.prototype=null===t?Object.create(t):(n.prototype=t.prototype,new n)}),o=this&&this.__assign||function(){return(o=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var a in t=arguments[n])Object.prototype.hasOwnProperty.call(t,a)&&(e[a]=t[a]);return e}).apply(this,arguments)},i=this&&this.__rest||function(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var a=0;for(r=Object.getOwnPropertySymbols(e);a<r.length;a++)t.indexOf(r[a])<0&&Object.prototype.propertyIsEnumerable.call(e,r[a])&&(n[r[a]]=e[r[a]])}return n};Object.defineProperty(t,"__esModule",{value:!0});var l=n(2),s=n(344),c=n(374),u=function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.renderConfirmModal=function(e){var n=e.onClose,r=t.props,a=(r.children,r.modalBody),c=r.modalHeader,u=r.modalHeaderDescription,m=i(r,["children","modalBody","modalHeader","modalHeaderDescription"]);return l.createElement(s.default,o({header:c,headerDescription:u,onClose:n},m),a)},t}return a(t,e),t.prototype.render=function(){return l.createElement(c.default,{modal:this.renderConfirmModal},this.props.children)},t}(l.PureComponent);t.default=u},374:function(e,t,n){"use strict";var r,a=this&&this.__extends||(r=function(e,t){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)t.hasOwnProperty(n)&&(e[n]=t[n])})(e,t)},function(e,t){function n(){this.constructor=e}r(e,t),e.prototype=null===t?Object.create(t):(n.prototype=t.prototype,new n)});Object.defineProperty(t,"__esModule",{value:!0});var o=n(2),i=function(e){function t(){var t=null!==e&&e.apply(this,arguments)||this;return t.mounted=!1,t.state={modal:!1},t.handleButtonClick=function(){t.setState({modal:!0})},t.handleFormSubmit=function(e){e&&e.preventDefault(),t.setState({modal:!0})},t.handleCloseModal=function(){t.mounted&&t.setState({modal:!1})},t}return a(t,e),t.prototype.componentDidMount=function(){this.mounted=!0},t.prototype.componentWillUnmount=function(){this.mounted=!1},t.prototype.render=function(){return o.createElement(o.Fragment,null,this.props.children({onClick:this.handleButtonClick,onFormSubmit:this.handleFormSubmit}),this.state.modal&&this.props.modal({onClose:this.handleCloseModal}))},t}(o.PureComponent);t.default=i},446:function(e,t,n){var r=n(393)((function(e,t,n){e[n?0:1].push(t)}),(function(){return[[],[]]}));e.exports=r},470:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(2),a=n(313);t.default=function(e){var t=e.className,n=e.fill,o=void 0===n?"currentColor":n,i=e.size;return r.createElement(a.default,{className:t,size:i},r.createElement("path",{d:"M12 9.25v2.5A2.25 2.25 0 0 1 9.75 14h-6.5A2.25 2.25 0 0 1 1 11.75v-6.5A2.25 2.25 0 0 1 3.25 3h5.5c.14 0 .25.11.25.25v.5c0 .14-.11.25-.25.25h-5.5C2.562 4 2 4.563 2 5.25v6.5c0 .688.563 1.25 1.25 1.25h6.5c.688 0 1.25-.563 1.25-1.25v-2.5c0-.14.11-.25.25-.25h.5c.14 0 .25.11.25.25zm3-6.75v4c0 .273-.227.5-.5.5a.497.497 0 0 1-.352-.148l-1.375-1.375L7.68 10.57a.27.27 0 0 1-.18.078.27.27 0 0 1-.18-.078l-.89-.89a.27.27 0 0 1-.078-.18.27.27 0 0 1 .078-.18l5.093-5.093-1.375-1.375A.497.497 0 0 1 10 2.5c0-.273.227-.5.5-.5h4c.273 0 .5.227.5.5z",style:{fill:o}}))}},587:function(e,t,n){"use strict";n.d(t,"b",(function(){return c})),n.d(t,"c",(function(){return u})),n.d(t,"a",(function(){return m}));var r=n(326),a=n.n(r),o=n(446),i=n.n(o),l=n(5);const s=["homepage","ci","issue","scm","scm_dev"];function c(e){return s.includes(e.type)}function u(e){const[t,n]=i()(e,c);return[...a()(t,e=>s.indexOf(e.type)),...a()(n,e=>e.name&&e.name.toLowerCase())]}function m(e){return c(e)?Object(l.translate)("project_links",e.type):e.name}},610:function(e,t,n){(function(e){!function(e){"use strict";e.exports.is_uri=n,e.exports.is_http_uri=r,e.exports.is_https_uri=a,e.exports.is_web_uri=o,e.exports.isUri=n,e.exports.isHttpUri=r,e.exports.isHttpsUri=a,e.exports.isWebUri=o;var t=function(e){return e.match(/(?:([^:\/?#]+):)?(?:\/\/([^\/?#]*))?([^?#]*)(?:\?([^#]*))?(?:#(.*))?/)};function n(e){if(e&&!/[^a-z0-9\:\/\?\#\[\]\@\!\$\&\'\(\)\*\+\,\;\=\.\-\_\~\%]/i.test(e)&&!/%[^0-9a-f]/i.test(e)&&!/%[0-9a-f](:?[^0-9a-f]|$)/i.test(e)){var n,r,a,o,i,l="",s="";if(l=(n=t(e))[1],r=n[2],a=n[3],o=n[4],i=n[5],l&&l.length&&a.length>=0){if(r&&r.length){if(0!==a.length&&!/^\//.test(a))return}else if(/^\/\//.test(a))return;if(/^[a-z][a-z0-9\+\-\.]*$/.test(l.toLowerCase()))return s+=l+":",r&&r.length&&(s+="//"+r),s+=a,o&&o.length&&(s+="?"+o),i&&i.length&&(s+="#"+i),s}}}function r(e,r){if(n(e)){var a,o,i,l,s="",c="",u="",m="";if(s=(a=t(e))[1],c=a[2],o=a[3],i=a[4],l=a[5],s){if(r){if("https"!=s.toLowerCase())return}else if("http"!=s.toLowerCase())return;if(c)return/:(\d+)$/.test(c)&&(u=c.match(/:(\d+)$/)[0],c=c.replace(/:\d+$/,"")),m+=s+":",m+="//"+c,u&&(m+=u),m+=o,i&&i.length&&(m+="?"+i),l&&l.length&&(m+="#"+l),m}}}function a(e){return r(e,!0)}function o(e){return r(e)||a(e)}}(e)}).call(this,n(31)(e))},709:function(e,t,n){"use strict";var r=this&&this.__assign||function(){return(r=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var a in t=arguments[n])Object.prototype.hasOwnProperty.call(t,a)&&(e[a]=t[a]);return e}).apply(this,arguments)},a=this&&this.__rest||function(e,t){var n={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(n[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var a=0;for(r=Object.getOwnPropertySymbols(e);a<r.length;a++)t.indexOf(r[a])<0&&Object.prototype.propertyIsEnumerable.call(e,r[a])&&(n[r[a]]=e[r[a]])}return n};Object.defineProperty(t,"__esModule",{value:!0});var o=n(2),i=n(710),l=n(711),s=n(470),c=n(712),u=n(713);t.default=function(e){var t=e.type,n=a(e,["type"]);switch(t){case"issue":return o.createElement(i.default,r({},n));case"homepage":return o.createElement(c.default,r({},n));case"ci":return o.createElement(l.default,r({},n));case"scm":return o.createElement(u.default,r({},n));default:return o.createElement(s.default,r({},n))}}},710:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(2),a=n(313);t.default=function(e){var t=e.className,n=e.fill,o=void 0===n?"currentColor":n,i=e.size;return r.createElement(a.default,{className:t,size:i},r.createElement("path",{d:"M13.5 9.5c1.003.033 1.466 1.952 0 2h-2.618L9.685 9.107 8 14.162 6.096 8.45l-.832 3.05-2.829-.002c-.984-.097-1.369-1.951.065-1.998h1.236l2.168-7.95L8 7.838l1.315-3.945L12.118 9.5H13.5z",style:{fill:o}}))}},711:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(2),a=n(313);t.default=function(e){var t=e.className,n=e.fill,o=void 0===n?"currentColor":n,i=e.size;return r.createElement(a.default,{className:t,size:i},r.createElement("path",{d:"M13.805 9.25c0 .016 0 .04-.008.055C13.133 12.07 10.852 14 7.969 14c-1.524 0-3-.602-4.11-1.656l-1.007 1.008a.497.497 0 0 1-.352.148.504.504 0 0 1-.5-.5V9.5c0-.273.227-.5.5-.5H6c.273 0 .5.227.5.5a.497.497 0 0 1-.148.352l-1.07 1.07a3.988 3.988 0 0 0 6.125-.828c.187-.305.28-.602.413-.914.04-.11.117-.18.235-.18h1.5c.14 0 .25.117.25.25zM14 3v3.5c0 .273-.227.5-.5.5H10a.504.504 0 0 1-.5-.5c0-.133.055-.258.148-.352l1.079-1.078A4.019 4.019 0 0 0 8 4c-1.39 0-2.68.719-3.406 1.906-.188.305-.282.602-.414.914-.04.11-.117.18-.235.18H2.391a.252.252 0 0 1-.25-.25v-.055C2.812 3.922 5.117 2 8 2c1.531 0 3.023.61 4.133 1.656l1.015-1.008A.497.497 0 0 1 13.5 2.5c.273 0 .5.227.5.5z",style:{fill:o}}))}},712:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(2),a=n(313);t.default=function(e){var t=e.className,n=e.fill,o=void 0===n?"currentColor":n,i=e.size;return r.createElement(a.default,{className:t,size:i},r.createElement("path",{d:"M13.002 8.848v4.168a.56.56 0 0 1-.556.555H9.11v-3.334H6.89v3.334H3.554a.56.56 0 0 1-.556-.555V8.848c0-.018.01-.035.01-.052L8 4.68l4.993 4.116c.009.017.009.034.009.052zm1.936-.6l-.538.643a.289.289 0 0 1-.183.096h-.026a.273.273 0 0 1-.182-.061L8 3.916l-6.009 5.01a.297.297 0 0 1-.208.06.289.289 0 0 1-.183-.095l-.538-.642a.285.285 0 0 1 .035-.391L7.34 2.656a1.07 1.07 0 0 1 1.32 0l2.119 1.772V2.735c0-.157.121-.278.278-.278h1.667c.156 0 .278.121.278.278v3.542l1.901 1.58c.113.096.13.279.035.392z",style:{fill:o}}))}},713:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=n(2),a=n(313);t.default=function(e){var t=e.className,n=e.fill,o=void 0===n?"currentColor":n,i=e.size;return r.createElement(a.default,{className:t,size:i},r.createElement("path",{d:"M12.557 4.545c.241.247.443.743.443 1.098v7.714c0 .355-.28.643-.625.643h-8.75A.634.634 0 0 1 3 13.357V2.643C3 2.288 3.28 2 3.625 2h5.833c.345 0 .827.208 1.068.455l2.031 2.09zM9.667 2.91v2.518h2.448a.86.86 0 0 0-.144-.275L9.934 3.058a.823.823 0 0 0-.267-.147zm2.5 10.232V6.286H9.458a.634.634 0 0 1-.625-.643V2.857h-5v10.286h8.334z",style:{fill:o}}))}},714:function(e,t,n){"use strict";var r=n(610);t.a=function(e){return/^(\/|scm:)/.test(e)||!!Object(r.isWebUri)(e)}},878:function(e,t,n){"use strict";n.d(t,"c",(function(){return o})),n.d(t,"b",(function(){return i})),n.d(t,"a",(function(){return l}));var r=n(8),a=n(321);function o(e){return Object(r.getJSON)("/api/project_links/search",{projectKey:e}).then(e=>e.links,a.a)}function i(e){return Object(r.post)("/api/project_links/delete",{id:e}).catch(a.a)}function l(e){return Object(r.postJSON)("/api/project_links/create",e).then(e=>e.link,a.a)}}}]);
//# sourceMappingURL=326.m.22f3175d.chunk.js.map