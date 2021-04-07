from ckan.model.follower import ModelFollowingModel
from typing import Dict, List, Type

import ckan.lib.dictization as d
import ckan.authz as authz
import ckan.model as model

def resource_dict_save(res_dict: Dict, context: Dict) -> model.Resource: ...
def package_resource_list_save(
    res_dicts: List[Dict], package: model.Package, context: Dict
) -> None: ...
def package_extras_save(
    extra_dicts: List[Dict], pkg: model.Package, context
) -> None: ...
def package_tag_list_save(
    tag_dicts: List[Dict], package: model.Package, context: Dict
) -> None: ...
def package_membership_list_save(
    group_dicts: List[Dict], package: model.Package, context
) -> None: ...
def relationship_list_save(
    relationship_dicts: List[Dict],
    package: model.Package,
    attr: str,
    context: Dict,
) -> None: ...
def package_dict_save(pkg_dict: Dict, context: Dict) -> model.Package: ...
def group_member_save(
    context: Dict, group_dict: Dict, member_table_name: str
) -> Dict: ...
def group_dict_save(
    group_dict: Dict, context: Dict, prevent_packages_update: bool = ...
) -> model.Group: ...
def user_dict_save(user_dict: Dict, context: Dict) -> model.User: ...
def package_api_to_dict(api1_dict: Dict, context: Dict) -> Dict: ...
def group_api_to_dict(api1_dict: Dict, context: Dict) -> Dict: ...
def task_status_dict_save(
    task_status_dict: Dict, context: Dict
) -> model.TaskStatus: ...
def activity_dict_save(
    activity_dict: Dict, context: Dict
) -> model.Activity: ...
def vocabulary_tag_list_save(
    new_tag_dicts: List[Dict], vocabulary_obj: model.Voacbulary, context: Dict
) -> None: ...
def vocabulary_dict_save(
    vocabulary_dict: Dict, context: Dict
) -> model.Vocabulary: ...
def vocabulary_dict_update(
    vocabulary_dict: Dict, context: Dict
) -> model.Vocabulary: ...
def tag_dict_save(tag_dict: Dict, context: Dict) -> model.Tag: ...
def follower_dict_save(
    data_dict: Dict, context: Dict, FollowerClass: Type[ModelFollowingModel]
) -> Type[ModelFollowingModel]: ...
def resource_view_dict_save(
    data_dict: Dict, context: Dict
) -> model.ResourceView: ...
def api_token_save(data_dict: Dict, context: Dict) -> model.ApiToken: ...