## index.html
<%inherit file="base.mako"/>

<%block name="script">
    <!-- Add more script imports here! -->
    <script src="/static/bootbox.min.js" xmlns="http://www.w3.org/1999/html"></script>
</%block>

<%block name="css">
    <!-- Add more css imports here! -->
    <link rel="stylesheet" type="text/css" href="/static/op_config.css">
</%block>

<%block name="title">
    OpenID Certification OP Test Tool Configuration
</%block>

<%block name="header">
    ${parent.header()}
</%block>

<%block name="headline">
    <div ng-controller="IndexCtrl" data-ng-init="loadExistingConfig()">
</%block>


<%block name="body">

    <div id="content">

        <h2>
            OpenID Connect Provider Certification - Test Instance Configuration
        </h2>

        <ul class="nav nav-tabs" ng-show="opConfig">
            <li role="presentation"
                ng-class="{'active': provider_tab_visible,
                           'disabled': true}">
                <a>Provider configuration</a>
            </li>

            <li role="presentation"
                ng-class="{'active': client_tab_visible,
                           'disabled': true}">
                <a>Client configuration</a>
            </li>
        </ul>

        <!-- HIDE EVERY THING UNDER THIS LINE UNTIL DATA IS STORED IN THE SESSION -->
        <!-- ################################################################################################# -->
        <div ng-show="opConfig" class="infoBlock">
            <div ng-show="provider_tab_visible">
                <h3>
                    Provider configuration:
                </h3>

                <span>
                    {{opConfig.fetchInfoFromServerDropDown.name}}
                </span>


                <select ng-model="opConfig.fetchInfoFromServerDropDown.value"
                        ng-options="v.type as v.name for v in opConfig.fetchInfoFromServerDropDown.values"
                        ng-change="switchBetweenProviderConfigElement();">
                </select>

                <br>

                <form class="row"
                      ng-show="opConfig.fetchDynamicInfoFromServer.showInputField == true"
                      novalidate
                      name="dynamic_disco_form">

                    <span class="col-sm-5">
                        {{opConfig.fetchDynamicInfoFromServer.input_field.label}}
                    </span>

                    <div class="col-sm-4">
                        <input type="text" maxlength="200" class="form-control" ng-model="opConfig.fetchDynamicInfoFromServer.input_field.value" name="issuer" issuer />
                    </div>

                    <span ng-show="dynamic_disco_form.issuer.$error.issuer"
                          class="col-sm-3 requiredText">
                        Issuer URL should not contain <i>.well-known/openid-configuration</i>
                    </span>
                </form>


                <button class="btn btn-default btn-sm"
                        ng-click="showModalWindowAddConfigFields();"
                        ng-show="opConfig.fetchStaticProviderInfo.showInputFields"
                        style="margin-bottom: 20px;">
                    Add static provider metadata field
                </button>

                <div ng-show="opConfig.fetchStaticProviderInfo.showInputFields">

                    <div ng-repeat="input_field in opConfig.fetchStaticProviderInfo.input_fields"
                         ng-show="input_field.show == true || input_field.required == true">
                        <hr>
                        <div class="row">

                            <div class="col-sm-5">
                                <br ng-show="input_field.isList">
                                {{input_field.label}}
                            </div>

                            <div ng-show="input_field.isList">
                                <div class="col-sm-3">
                                    New element:
                                    <form>
                                        <div class="input-group">
                                            <input type="text" maxlength="200" class="form-control" id="input_{{input_field.id}}">
                                            <span class="input-group-btn">
                                                <button class="btn btn-default btn-sm"
                                                        ng-click="addStaticProviderInfoElement(input_field.id)">
                                                    Add
                                                </button>
                                            </span>
                                        </div>
                                    </form>
                                </div>

                                <div class="col-sm-4">
                                    Added elements:
                                    <form ng-repeat="element in input_field.values">
                                        <div class="input-group">
                                            <input type="text" maxlength="200" ng-model="element.value" class="form-control">
                                            <span class="input-group-btn">
                                                <button class="btn btn-danger btn-sm"
                                                        ng-click="removeStaticProviderInfoElement($index, input_field.id)">
                                                    X
                                                </button>
                                            </span>
                                        </div>
                                    </form>
                                </div>
                            </div>

                            <div class="col-sm-3" ng-show="!input_field.isList"></div>

                            <div class="col-sm-4" ng-show="!input_field.isList">
                                <input type="text" maxlength="200" class="form-control" ng-model="input_field.values">
                            </div>
                        </div>
                    </div>
                </div>

                <span class="requiredText" ng-show="opConfig.fetchStaticProviderInfo.showInputFields ||
                                                    opConfig.fetchDynamicInfoFromServer.showInputField">
                    * Required fields
                </span>

                <br>
                <button class="btn btn-primary btn-sm" disabled="disabled">
                    Previous
                </button>

                <button class="btn btn-primary btn-sm"
                        ng-click="show_client_config()"
                        ng-disabled="dynamic_disco_form.$invalid || !contains_required_provider_info()">
                    Next
                </button>
            </div>

            <!-- ################################################################################################# -->
            <div ng-show="client_tab_visible">
                <h3>
                    Client configuration:
                </h3>

                <div class="row">
                    <div class="col-sm-12">
                        <span>
                            {{opConfig.dynamicClientRegistrationDropDown.label}}
                        </span>
                        <select ng-model="opConfig.dynamicClientRegistrationDropDown.value"
                                ng-options="v.type as v.name for v in opConfig.dynamicClientRegistrationDropDown.values"
                                ng-disabled="!contains_redirect_url">
                        </select>
                    </div>
                </div>


                <div class="row"
                     ng-repeat="textField in opConfig.supportsStaticClientRegistrationTextFields"
                     ng-show="opConfig.dynamicClientRegistrationDropDown.value == 'no'">
                    <div class="col-sm-4">
                        {{textField.label}}
                    </div>

                    <form class="col-sm-8">
                        <input type="text" maxlength="200" ng-model="textField.textFieldContent" ng-readonly="textField.disabled"
                               class="form-control">
                    </form>
                </div>
            <span class="requiredText"
                  ng-show="opConfig.dynamicClientRegistrationDropDown.value == 'no'">
                * Required info
            </span>


                <div class="row singleLine">
                    <div class="col-sm-12">
                <span>
                    {{opConfig.clientSubjectType.label}}
                </span>

                        <select ng-model="opConfig.clientSubjectType.value"
                                ng-options="v.type as v.name for v in opConfig.clientSubjectType.values">
                        </select>
                    </div>
                </div>

                <div class="row singleLine">
                    <div class="col-sm-12">
                    <span>
                        {{opConfig.responseTypeDropDown.label}}
                    </span>

                        <select ng-model="opConfig.responseTypeDropDown.value"
                                ng-options="v.type as v.name for v in opConfig.responseTypeDropDown.values">
                        </select>
                    </div>
                </div>

                <div class="row singleLine">
                <span class="col-sm-3">
                    <span class="glyphicon glyphicon-info-sign infoIcon"
                          title="Enter all the features which the OP supports. If no feature is selected that means the OP does not support JWT"
                          data-toggle="tooltip"
                          data-placement="right"
                          directive-callback="">
                    </span>

                    {{opConfig.signingEncryptionFeaturesCheckboxes.label}}
                </span>

                    <div class="col-sm-9">
                        <fieldset ng-repeat="feature in opConfig.signingEncryptionFeaturesCheckboxes.features">
                            <input type="checkbox"
                                   value="{{feature.name}}"
                                   ng-model="feature.selected"/>
                            {{feature.name}}
                        </fieldset>
                    </div>
                </div>

                <h4>
            <span class="glyphicon glyphicon-info-sign infoIcon"
                  title="The request parameters are used in specific tests. The ID of the test which uses a request parameter is specified after every parameter"
                  data-toggle="tooltip"
                  data-placement="right"
                  directive-callback=""></span>

                    Test specific request parameters:
                </h4>

                <div class="row">
                    <div class="col-sm-3">
            <span class="glyphicon glyphicon-info-sign infoIcon"
                  title="Hint to the Authorization Server about the login identifier the End-User might use to log in (if necessary). This hint can be used by an RP if it first asks the End-User for their e-mail address (or other identifier) and then wants to pass that value as a hint to the discovered authorization service. It is RECOMMENDED that the hint value match the value used for discovery. This value MAY also be a phone number in the format specified for the phone_number Claim. The use of this parameter is left to the OP's discretion"
                  data-toggle="tooltip"
                  data-placement="right"
                  directive-callback=""></span>

                        <span>Login hint</span>
                    </div>

                    <form class="col-sm-3">
                        <input type="text" maxlength="200" ng-model="opConfig.loginHint" class="form-control">
                    </form>

                    <div class="col-sm-6">
                        E.g. bob@example.com
                    </div>
                </div>

                ##### UI locales ######

                <div class="row">
                <span class="col-sm-3">
                    <span class="glyphicon glyphicon-info-sign infoIcon"
                          title="End-User's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value 'fr-CA fr en' represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider."
                          data-toggle="tooltip"
                          data-placement="right"
                          directive-callback=""></span>

                    UI locales
                </span>

                    <div class="col-sm-3">
                        <input type="text" maxlength="200" ng-model="opConfig.uiLocales" class="form-control">
                    </div>

                    <div class="col-sm-6">
                        E.g. en se
                    </div>
                </div>

                <div class="row">

                    <div class="col-sm-3">
                    <span class="glyphicon glyphicon-info-sign infoIcon"
                          title="End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider."
                          data-toggle="tooltip"
                          data-placement="right"
                          directive-callback=""></span>

                        Claims locales

                    </div>

                    <div class="col-sm-3">
                        <input type="text" maxlength="200" ng-model="opConfig.claimsLocales" class="form-control">
                    </div>

                    <div class="col-sm-6">
                        E.g. en se
                    </div>

                </div>

                <div class="row">
                    <div class="col-sm-3">
                        <span class="glyphicon glyphicon-info-sign infoIcon"
                              title="Requested Authentication Context Class Reference values. Space-separated string that specifies the acr values that the Authorization Server is being requested to use for processing this authentication request, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value, as specified in Section 2.1.2.1. The acr Claim is requested as a Voluntary Claim by this parameter."
                              data-toggle="tooltip"
                              data-placement="right"
                              directive-callback="">
                        </span>

                        Acr values

                    </div>

                    <div class="col-sm-3">
                        <input type="text" maxlength="200" ng-model="opConfig.acrValues" class="form-control">
                    </div>

                    <div class="col-sm-6">
                        E.g. 2 1
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-3">
                        <span class="glyphicon glyphicon-info-sign infoIcon"
                              title="The RP would make the following WebFinger request to discover the Issuer location using the URL syntax. For example https://example.com/joe"
                              data-toggle="tooltip"
                              data-placement="right"
                              directive-callback="">
                        </span>

                        Webfinger url

                    </div>

                    <div class="col-sm-3">
                        <input type="text" maxlength="200" ng-model="opConfig.webfinger_url" class="form-control">
                    </div>

                    <div class="col-sm-6">
                        https://example.com/bob
                    </div>
                </div>

                <div class="row">
                    <div class="col-sm-3">
                        <span class="glyphicon glyphicon-info-sign infoIcon"
                              title="The RP would make the following WebFinger request to discover the Issuer location using the e-mail address syntax. For example joe@example.com"
                              data-toggle="tooltip"
                              data-placement="right"
                              directive-callback="">
                        </span>

                       Webfinger email

                    </div>

                    <div class="col-sm-3">
                        <input type="text" maxlength="200" ng-model="opConfig.webfinger_email" class="form-control">
                    </div>

                    <div class="col-sm-6">
                        E.g. bob@example.com
                    </div>
                </div>

                <button class="btn btn-primary btn-sm" ng-click="show_provider_config()">
                    Previous
                </button>

                <button class="btn btn-primary btn-sm"
                        ng-click="saveConfigurations()"
                        ng-disabled="!containsRequiredClientInfo()">
                    Submit
                </button>

                <!-- ################################################################################################# -->
            </div>
        </div>
    </div>

    <div class="modal fade" id="modalWindowAddConfigFields" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
         aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title">Static metadata fields</h4>
                </div>

                Mark the fields you want to show on the config page

                <div id="advancedFieldTable">
                    <table class="table table-striped">
                        <tr ng-repeat="input_field in opConfig.fetchStaticProviderInfo.input_fields">
                            <td><input type="checkbox" ng-model="input_field.show" ng-disabled="input_field.required">
                            </td>
                            <td>{{input_field.label}}</td>
                        <tr>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="modalWindowUploadConfigurationFile" tabindex="-1" role="dialog"
         aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title">Upload configuration</h4>
                </div>
                <div class="modal-body">
                    <input type="file" name="file" id="targetFile">
                    <button class="btn btn-primary btn-sm" ng-click="request_upload_config_file();">Upload configurations
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal window containg iframe-->
    <div class="modal fade" id="modalWindowInteraction" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
         aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content" id="modalWindowHTMLContent">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title">Show html dialog</h4>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Start here-->
    <div class="modal fade bs-example-modal-sm" id="myPleaseWait" tabindex="-1"
        role="dialog" aria-hidden="true" data-backdrop="static">
        <div class="modal-dialog modal-sm">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">
                        <span class="glyphicon glyphicon-time">
                        </span>Please wait while your infomation is being stored
                     </h4>
                </div>
                <div class="modal-body">
                    <img src="static/loader.gif" alt="Loading screen" align="center" class="centeralBlock">
                </div>
            </div>
        </div>
    </div>
    <!-- Modal ends Here -->

</%block>

<%block name="footer">
    </div>

    <script type="text/javascript" src="/static/op_config.js"></script>
    ${parent.footer()}
</%block>