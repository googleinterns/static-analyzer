(window.webpackJsonp=window.webpackJsonp||[]).push([[388],{1915:function(e,t,n){"use strict";n.r(t),n.d(t,"default",(function(){return h}));var a=n(2),r=n(328),s=n(316),c=n.n(s),o=n(5),i=n(605),l=n(304),m=n(310),p=n(377);class u extends a.PureComponent{constructor(){super(...arguments),this.mounted=!1,this.state={encrypting:!1,generating:!1,value:""},this.handleChange=e=>{this.setState({value:e.currentTarget.value})},this.handleEncrypt=e=>{e.preventDefault(),this.setState({encrypting:!0}),Object(i.b)(this.state.value).then(({encryptedValue:e})=>{this.mounted&&this.setState({encryptedValue:e,encrypting:!1})},()=>{this.mounted&&this.setState({encrypting:!1})})},this.handleGenerateSecretKey=e=>{e.preventDefault(),this.setState({generating:!0}),this.props.generateSecretKey().then(this.stopGenerating,this.stopGenerating)},this.stopGenerating=()=>{this.mounted&&this.setState({generating:!1})}}componentDidMount(){this.mounted=!0}componentWillUnmount(){this.mounted=!1}render(){const{encryptedValue:e,encrypting:t,generating:n}=this.state;return a.createElement("div",{id:"encryption-form-container"},a.createElement("div",{className:"spacer-bottom"},Object(o.translate)("encryption.form_intro")),a.createElement("form",{className:"big-spacer-bottom",id:"encryption-form",onSubmit:this.handleEncrypt},a.createElement("textarea",{autoFocus:!0,className:"abs-width-600",id:"encryption-form-value",onChange:this.handleChange,required:!0,rows:5,value:this.state.value}),a.createElement("div",{className:"spacer-top"},a.createElement(m.SubmitButton,{disabled:t||n},Object(o.translate)("encryption.encrypt")),a.createElement(c.a,{className:"spacer-left",loading:t}))),e&&a.createElement("div",null,a.createElement("span",{className:"little-spacer-right"},Object(o.translate)("encryption.encrypted_value")),a.createElement("input",{className:"input-clear input-code input-super-large",id:"encrypted-value",readOnly:!0,type:"text",value:e}),a.createElement(p.ClipboardButton,{className:"little-spacer-left",copyValue:e})),a.createElement("form",{className:"huge-spacer-top bordered-top",id:"encryption-new-key-form",onSubmit:this.handleGenerateSecretKey},a.createElement("p",{className:"big-spacer-top spacer-bottom"},a.createElement(l.FormattedMessage,{defaultMessage:Object(o.translate)("encryption.form_note"),id:"encryption.form_note",values:{moreInformationLink:a.createElement("a",{href:"https://redirect.sonarsource.com/doc/settings-encryption.html",rel:"noopener noreferrer",target:"_blank"},Object(o.translate)("more_information"))}})),a.createElement(m.SubmitButton,{disabled:n||t},Object(o.translate)("encryption.generate_new_secret_key")," "),a.createElement(c.a,{className:"spacer-left",loading:n})))}}class d extends a.PureComponent{constructor(){super(...arguments),this.mounted=!1,this.state={submitting:!1},this.handleSubmit=e=>{e.preventDefault(),this.setState({submitting:!0}),this.props.generateSecretKey().then(this.stopSubmitting,this.stopSubmitting)},this.stopSubmitting=()=>{this.mounted&&this.setState({submitting:!1})}}componentDidMount(){this.mounted=!0}componentWillUnmount(){this.mounted=!1}render(){const{secretKey:e}=this.props,{submitting:t}=this.state;return a.createElement("div",{id:"generate-secret-key-form-container"},e?a.createElement(a.Fragment,null,a.createElement("div",{className:"big-spacer-bottom"},a.createElement("h3",{className:"spacer-bottom"},Object(o.translate)("encryption.secret_key")),a.createElement("input",{className:"input-clear input-code input-large",id:"secret-key",readOnly:!0,type:"text",value:e}),a.createElement(p.ClipboardButton,{className:"little-spacer-left",copyValue:e})),a.createElement("h3",{className:"spacer-bottom"},Object(o.translate)("encryption.how_to_use")),a.createElement("div",{className:"markdown"},a.createElement("ul",null,a.createElement("li",null,a.createElement(l.FormattedMessage,{defaultMessage:Object(o.translate)("encryption.how_to_use.content1"),id:"encryption.how_to_use.content1",values:{secret_file:a.createElement("code",null,"~/.sonar/sonar-secret.txt"),property:a.createElement("code",null,"sonar.secretKeyPath"),propreties_file:a.createElement("code",null,"conf/sonar.properties")}})),a.createElement("li",null,Object(o.translate)("encryption.how_to_use.content2")),a.createElement("li",null,a.createElement(l.FormattedMessage,{defaultMessage:Object(o.translate)("encryption.how_to_use.content3"),id:"encryption.how_to_use.content3",values:{property:a.createElement("code",null,"sonar.secretKeyPath")}})),a.createElement("li",null,Object(o.translate)("encryption.how_to_use.content4"))))):a.createElement("form",{id:"generate-secret-key-form",onSubmit:this.handleSubmit},a.createElement("p",{className:"spacer-bottom"},a.createElement(l.FormattedMessage,{defaultMessage:Object(o.translate)("encryption.secret_key_description"),id:"encryption.secret_key_description",values:{moreInformationLink:a.createElement("a",{href:"https://redirect.sonarsource.com/doc/settings-encryption.html",rel:"noopener noreferrer",target:"_blank"},Object(o.translate)("more_information"))}})),a.createElement(m.SubmitButton,{disabled:t},Object(o.translate)("encryption.generate_secret_key")),a.createElement(c.a,{className:"spacer-left",loading:t})))}}class h extends a.PureComponent{constructor(){super(...arguments),this.state={loading:!0},this.mounted=!1,this.checkSecretKey=()=>{Object(i.a)().then(({secretKeyAvailable:e})=>{this.mounted&&this.setState({loading:!1,secretKeyAvailable:e})},()=>{this.mounted&&this.setState({loading:!1})})},this.generateSecretKey=()=>Object(i.c)().then(({secretKey:e})=>{this.mounted&&this.setState({secretKey:e,secretKeyAvailable:!1})})}componentDidMount(){this.mounted=!0,this.checkSecretKey()}componentWillUnmount(){this.mounted=!1}render(){const{loading:e,secretKey:t,secretKeyAvailable:n}=this.state;return a.createElement("div",{className:"page page-limited",id:"encryption-page"},a.createElement(r.a,{defer:!1,title:Object(o.translate)("property.category.security.encryption")}),a.createElement("header",{className:"page-header"},a.createElement("h1",{className:"page-title"},Object(o.translate)("property.category.security.encryption")),a.createElement(c.a,{loading:e})),!e&&!n&&a.createElement(d,{generateSecretKey:this.generateSecretKey,secretKey:t}),n&&a.createElement(u,{generateSecretKey:this.generateSecretKey}))}}}}]);
//# sourceMappingURL=388.m.3d3ff1ca.chunk.js.map