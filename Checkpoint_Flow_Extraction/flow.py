class RuleIntermediator:
    @staticmethod
    def fetch_rules(filtered_list):
        groups = {}
        # Extract uids for each policy
        # and classify them in a dict
        for rule, name, layer in [
            (a["rule"]["uid"], a["package"]["name"], a["layer"]["name"])
            for a in filtered_list
        ]:
            if name in groups:
                groups[name]["uids"].append(rule)
            else:
                groups[name] = {"uids": [rule], "layer": layer}

        return groups

    @staticmethod
    def filter_layer_type(rule_list):
        return list(filter(lambda d: d["layer"]["type"] == "access-layer", rule_list))

    @staticmethod
    def order_by_package_name(rule_list):
        return sorted(rule_list, key=lambda k: k["package"]["name"])


class AccessRule:

    # Constructor
    def __init__(
        self, uid, name, policy, source, destination, service, action, comment
    ):
        self.uid = uid  # The rule UID
        self.name = name  # The rule name
        self.policy = policy  # The oolicy name
        self.source = source  # The source ip address(es)
        self.destination = destination  # The destination ip address(es)
        self.service = service  # The port(s) in the rule
        self.action = action  # The action of the rule
        self.comment = comment  # The comment of the rule

    @staticmethod
    def getInstance(response, policy):
        return AccessRule(
            uid=response["uid"],
            name=response["name"],
            policy=policy,
            source=response["source"],
            destination=response["destination"],
            service=response["service"],
            action=response["action"]["name"],
            comment=response["comments"],
        )

