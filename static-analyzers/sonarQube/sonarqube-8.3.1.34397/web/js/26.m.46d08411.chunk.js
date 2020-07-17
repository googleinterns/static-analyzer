(window.webpackJsonp=window.webpackJsonp||[]).push([[26],{1056:function(e,t,n){var r=n(311),o=n(1057);"string"==typeof(o=o.__esModule?o.default:o)&&(o=[[e.i,o,""]]);var c={insert:"head",singleton:!1},l=(r(o,c),o.locals?o.locals:{});e.exports=l},1057:function(e,t,n){(t=n(312)(!1)).push([e.i,".markdown-content .alert{margin-bottom:8px;border:1px solid;border-radius:2px}.markdown-content .alert.is-inline{display:inline-flex}.markdown-content .alert:empty{display:none}.markdown-content .alert-danger,.markdown-content .alert-error{border-color:#f4b1b0;background-color:#f2dede;color:#862422}.markdown-content .alert-danger .alert-icon,.markdown-content .alert-error .alert-icon{border-color:#f4b1b0}.markdown-content .alert-warning{border-color:#faebcc;background-color:#fcf8e3;color:#6f4f17}.markdown-content .alert-warning .alert-icon{border-color:#faebcc}.markdown-content .alert-info{border-color:#b1dff3;background-color:#d9edf7;color:#0e516f}.markdown-content .alert-info .alert-icon{border-color:#b1dff3}.markdown-content .alert-success{border-color:#d6e9c6;background-color:#dff0d8;color:#215821}.markdown-content .alert-success .alert-icon{border-color:#d6e9c6}",""]),e.exports=t},337:function(e,t,n){"use strict";function r(e,t){const n=e.displayName||e.name||"Component";return"".concat(t,"(").concat(n,")")}n.d(t,"a",(function(){return r}))},413:function(e,t,n){"use strict";n.d(t,"a",(function(){return a}));var r=n(2),o=n(317),c=n(319),l=n(337);function a(e){class t extends r.Component{render(){return r.createElement(e,Object.assign({},this.props))}}return t.displayName=Object(l.a)(e,"withAppState"),Object(o.connect)((function(e){return{appState:Object(c.getAppState)(e)}}))(t)}},463:function(e,t,n){"use strict";n.r(t),n.d(t,"default",(function(){return $}));var r=n(309),o=n(2),c=n(1173),l=n.n(c),a=n(1192),s=n.n(a),i=n(778),u=n.n(i),d=n(1215),p=n.n(d),h=n(1216),m=n.n(h),f=n(839),b=n.n(f),g=n(1227),k=n.n(g),O=n(426),w=n(431),y=n.n(w);class E extends o.PureComponent{constructor(){super(...arguments),this.state={open:!1},this.handleClick=e=>{this.setState(e=>({open:!e.open})),e.stopPropagation(),e.preventDefault()}}renderTitle(e){return o.createElement("a",{"aria-expanded":this.state.open,"aria-haspopup":!0,className:"link-no-underline",href:"#",onClick:this.handleClick},o.createElement(y.a,{className:"text-middle little-spacer-right",open:this.state.open}),e.props?e.props.children:e)}render(){const e=o.Children.toArray(this.props.children);if(e.length<1)return null;const t=o.Children.toArray(e[0].props.children);return t.length<2?null:o.createElement("div",{className:"collapse-container"},this.renderTitle(t[0]),this.state.open&&t.slice(1))}}var v=n(336);function j(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},c=Object.keys(e);for(r=0;r<c.length;r++)n=c[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var c=Object.getOwnPropertySymbols(e);for(r=0;r<c.length;r++)n=c[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}function C(e){const{alt:t,src:n}=e,r=j(e,["alt","src"]);return o.createElement("img",Object.assign({alt:t,className:"max-width-100",src:Object(v.getBaseUrl)()+"/images/embed-doc"+n},r))}var x=n(314),S=n(470),A=n.n(S),N=n(22),P=n(413);function _(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},c=Object.keys(e);for(r=0;r<c.length;r++)n=c[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var c=Object.getOwnPropertySymbols(e);for(r=0;r<c.length;r++)n=c[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}class H extends o.PureComponent{constructor(){super(...arguments),this.handleClickOnAnchor=e=>{const{customProps:t,href:n="#"}=this.props;t&&t.onAnchorClick&&t.onAnchorClick(n,e)}}render(){const e=this.props,{appState:t,children:n,href:r,customProps:c}=e,l=_(e,["appState","children","href","customProps"]);if(r&&r.startsWith("#"))return o.createElement("a",{href:"#",onClick:this.handleClickOnAnchor},n);if(r&&r.startsWith("/")){if(r.startsWith("/#sonarcloud#/"))return o.createElement(T,{url:r},n);if(r.startsWith("/#sonarqube#/"))return o.createElement(W,{url:r},n);if(r.startsWith("/#sonarqube-admin#/"))return o.createElement(D,{canAdmin:t.canAdmin,url:r},n);{const e="/documentation"+r;return o.createElement(x.Link,Object.assign({to:e},l),n)}}return o.createElement(o.Fragment,null,o.createElement("a",Object.assign({href:r,rel:"noopener noreferrer",target:"_blank"},l),n),o.createElement(A.a,{className:"text-muted little-spacer-left little-spacer-right text-baseline",size:12}))}}var L=Object(P.a)(H);function T({children:e,url:t}){if(Object(N.isSonarCloud)()){const n="/".concat(t.substr("/#sonarcloud#/".length));return o.createElement(x.Link,{to:n},e)}return o.createElement(o.Fragment,null,e)}function W({children:e,url:t}){if(Object(N.isSonarCloud)())return o.createElement(o.Fragment,null,e);{const n="/".concat(t.substr("/#sonarqube#/".length));return o.createElement(x.Link,{target:"_blank",to:n},e)}}function D({canAdmin:e,children:t,url:n}){if(Object(N.isSonarCloud)()||!e)return o.createElement(o.Fragment,null,t);{const e="/".concat(n.substr("/#sonarqube-admin#/".length));return o.createElement(x.Link,{target:"_blank",to:e},t)}}n(1056);var q=n(503),F=n.n(q),I=n(364),M=n.n(I),U=n(465),z=n(1228),J=n.n(z),B=n(5),K=n(1234),R=n.n(K);function Y(){return this.use(b.a),function(e){const t=R()(e,{heading:"doctoc",maxDepth:2});null!==t.index&&-1!==t.index&&t.map?e.children=[t.map]:e.children=[]}}class G extends o.PureComponent{constructor(e){super(e),this.node=null,this.state={anchors:[]},this.scrollHandler=()=>{const e=Object(U.findDOMNode)(this);if(!e||!e.parentNode)return;const t=e.parentNode.querySelectorAll("h2[id]"),n=window.pageYOffset||document.body.scrollTop;let r;for(let e=0,o=t.length;e<o&&!(t.item(e).offsetTop>n+120);e++)r="#".concat(t.item(e).id);this.setState({highlightAnchor:r})},this.debouncedScrollHandler=M()(this.scrollHandler)}static getDerivedStateFromProps(e){const{content:t}=e;return{anchors:G.getAnchors(t)}}componentDidMount(){window.addEventListener("scroll",this.debouncedScrollHandler,!0),this.scrollHandler()}componentWillUnmount(){window.removeEventListener("scroll",this.debouncedScrollHandler,!0)}render(){const{anchors:e,highlightAnchor:t}=this.state;return 0===e.length?null:o.createElement("div",{className:"markdown-toc"},o.createElement("div",{className:"markdown-toc-content"},o.createElement("h4",null,Object(B.translate)("documentation.on_this_page")),e.map(e=>o.createElement("a",{className:r({active:t===e.href}),href:e.href,key:e.title,onClick:t=>{this.props.onAnchorClick(e.href,t)}},e.title))))}}G.getAnchors=F()(e=>{const t=u()().use(J.a).use(Y).processSync("\n## doctoc\n"+e);if(t&&t.contents.props.children){let e=t.contents,n=10;for(;n&&e.props.children.length&&"ul"!==e.type;)e=e.props.children[0],n--;if("ul"===e.type&&e.props.children.length)return e.props.children.map(e=>{if("string"==typeof e)return null;const t=e.props.children[0];return{href:t.props.href,title:t.props.children[0]}}).filter(e=>e)}return[]});var Q=n(840),V=n.n(Q);function X(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},c=Object.keys(e);for(r=0;r<c.length;r++)n=c[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var c=Object.getOwnPropertySymbols(e);for(r=0;r<c.length;r++)n=c[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}function Z(e){let{children:t,customProps:n,href:r}=e,c=X(e,["children","customProps","href"]);return n&&V()(n,(e,t)=>{r&&(r=r.replace("#".concat(t,"#"),encodeURIComponent(e)))}),r&&r.startsWith("/")?(r=r.startsWith("/#sonarcloud#/")?"/".concat(r.substr("/#sonarcloud#/".length)):"/documentation/".concat(r.substr(1)),o.createElement(x.Link,Object.assign({rel:"noopener noreferrer",target:"_blank",to:r},c),t)):o.createElement(o.Fragment,null,o.createElement("a",Object.assign({href:r,rel:"noopener noreferrer",target:"_blank"},c),t),o.createElement(A.a,{className:"little-spacer-left little-spacer-right text-baseline",size:12}))}class $ extends o.PureComponent{constructor(){super(...arguments),this.node=null,this.handleAnchorClick=(e,t)=>{if(this.node){const n=this.node.querySelector(e);n&&(t.preventDefault(),Object(O.scrollToElement)(n,{bottomOffset:window.innerHeight-80}),history.pushState&&history.pushState(null,"",e))}}}render(){const{childProps:e,content:t,className:n,title:c,stickyToc:a,isTooltip:i}=this.props,d=u()();return d.use(p.a,{danger:{classes:"alert alert-danger"},warning:{classes:"alert alert-warning"},info:{classes:"alert alert-info"},success:{classes:"alert alert-success"},collapse:{classes:"collapse"}}).use(m.a,{allowDangerousHTML:!0}).use(l.a).use(s.a,{createElement:o.createElement,components:{div:te,a:i?ee(Z,e):ee(L,{onAnchorClick:this.handleAnchorClick}),img:C,"update-center":({updatecenterkey:e})=>o.createElement(k.a,{updateCenterKey:e})}}).use(b.a),o.createElement("div",{className:r("markdown",n,{"has-toc":a}),ref:e=>this.node=e},o.createElement("div",{className:"markdown-content"},void 0!==c&&o.createElement("h1",{className:"documentation-title"},c),d.processSync(t).contents),a&&o.createElement(G,{content:t,onAnchorClick:this.handleAnchorClick}))}}function ee(e,t){return function(n){return o.createElement(e,Object.assign({customProps:t},n))}}function te(e){return e.className?e.className.includes("collapse")?o.createElement(E,null,e.children):o.createElement("div",{className:r("cut-margins",e.className)},e.children):e.children}}}]);
//# sourceMappingURL=26.m.46d08411.chunk.js.map