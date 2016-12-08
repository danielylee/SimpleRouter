# Final Skeleton
#
# Hints/Reminders from Lab 4:
#
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. The following modifications have
    # been made from Lab 4:
    #   - port_on_switch represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    if packet.find('ipv4') is None:
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
        msg.data = packet_in
        self.connection.send(msg)
    else:
        if (switch_id == 4):
            if (port_on_switch == 6 and packet.payload.find('icmp')):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.data = packet_in
                self.connection.send(msg)
        elif packet.find('ipv4') is not None and port_on_switch == 6:
            if packet.find('ipv4').dstip == ('10.0.1.10'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.actions.append(of.ofp_action_output(port = 3))
                msg.data = packet_in
                self.connection.send(msg)
            elif packet.find('ipv4').dstip == ('10.0.2.20'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.actions.append(of.ofp_action_output(port = 4))
                msg.data = packet_in
                self.connection.send(msg)
            elif packet.find('ipv4').dstip == ('10.0.3.30'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.actions.append(of.ofp_action_output(port = 5))
                msg.data = packet_in
                self.connection.send(msg)
            elif packet.find('ipv4').dstip == ('10.0.4.10'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.data = packet_in
                self.connection.send(msg)
        else:
            if packet.find('ipv4').dstip == ('10.0.1.10'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.actions.append(of.ofp_action_output(port = 3))
                msg.data = packet_in
                self.connection.send(msg)
            elif packet.find('ipv4').dstip == ('10.0.2.20'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.actions.append(of.ofp_action_output(port = 4))
                msg.data = packet_in
                self.connection.send(msg)
            elif packet.find('ipv4').dstip == ('10.0.3.30'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.actions.append(of.ofp_action_output(port = 5))
                msg.data = packet_in
                self.connection.send(msg)
            elif packet.find('ipv4').dstip == ('10.0.4.10'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.actions.append(of.ofp_action_output(port = 7))
                msg.data = packet_in
                self.connection.send(msg)
            elif packet.find('ipv4').dstip == ('172.16.10.100'):
                msg = of.ofp_flow_mod()
                msg.match = of.ofp_match.from_packet(packet)
                msg.idle_timeout = 30
                msg.hard_timeout = 30
                msg.actions.append(of.ofp_action_output(port = 6))
                msg.data = packet_in
                self.connection.send(msg)
        else:
        # check for IP traffic
            if packet.find('ipv4') is not None:
                if port_on_switch == 1:
                    msg = of.ofp_flow_mod()
                    msg.match = of.ofp_match.from_packet(packet)
                    msg.idle_timeout = 30
                    msg.hard_timeout = 30
                    msg.actions.append(of.ofp_action_output(port = 2))
                    msg.data = packet_in
                    self.connection.send(msg)
                else:
                    msg = of.ofp_flow_mod()
                    msg.match = of.ofp_match.from_packet(packet)
                    msg.idle_timeout = 30
                    msg.hard_timeout = 30
                    msg.actions.append(of.ofp_action_output(port = 1))
                    msg.data = packet_in
                    self.connection.send(msg)

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
