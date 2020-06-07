# Keep track of contributions from group members

class MemberNotFoundError(Exception):
    pass

class DateNotFoundError(Exception):
    pass


class Club:
    # members = ["Judy", "Vanilla Bear"]
    def __init__(self, name, description):
        #super(Group, self).__init__()
        self.name = name
        self.description = description
    def description(self):
        return "A tech club that tracks hooligans."
    
    def add_member(self, member):
        """Add a member to the club"""
        self.member = member

    def add_contribution(self, member, date, summary):
        """Add a contribution to a member"""
        self.member = member
        self.date = date
        self.summary = summary
        return self.member, self.summary


    def count_contributions(self, member):
        """Counts the number of contributions of a member"""
        self.member = member
        count = len(self.summary)
        return count
        

    def find_summary(self, member, date):
        """Find the summary of a member at a centain date."""
        self.member = member
        self.date = date
        return self.summary


club1 = Club("FriendsForever","A tech club that holds lifelong friendships")
club1.add_member("Judy")
club1.add_member("Vanilla Bear")
club1.add_contribution("Vanilla Bear","Jan 2","Contacted Over The Luna Designs for art.")
club1.add_contribution("Judy","Jan 5","Organized first meeting.")
club1.add_contribution("Judy","Jan 7","Went shopping.")
club1.add_contribution("Judy","Jan 14","Organized second meeting.")
club1.add_contribution("Vanilla Bear","Jan 21","Sent payment to Over The Luna Designs.")

