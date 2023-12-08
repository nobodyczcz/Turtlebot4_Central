import abc
from typing import Dict, Tuple, List

from Position import Position
from Agent import Agent


class ExecutionPolicy(abc.ABC):
    """
    Abstract base class for execution policies.
    """

    @abc.abstractmethod
    def get_next_position(self, agent_id: int) -> Tuple[Position, int]:
        """
        Abstract method to get the next position.

        Args:
            agent_id (int): The index of the current position.

        Returns:
            Tuple[Position, int]: The next position and the time to reach it.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, data: Dict) -> None:
        """
        Abstract method to update the execution policy.

        Args:
            data (Dict): The data to update the policy.
        """
        raise NotImplementedError

class OnlineExecutionPolicy(abc.ABC):
    """
    Abstract base class for online execution policies that can extend plans.
    """

    @abc.abstractmethod
    def get_next_position(self, agent_id: int) -> Tuple[Position, int]:
        """
        Abstract method to get the next position.

        Args:
            agent_id (int): The index of the current position.

        Returns:
            Tuple[Position, int]: The next position and the time to reach it.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, data: Dict) -> None:
        """
        Abstract method to update the execution policy.

        Args:
            data (Dict): The data to update the policy.
        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_agent_locations(self) -> List[Tuple[Position, int]]:
        """
        Abstract method to get the final committed positions of agents to extend plans on

        Returns:
            List[Tuple[Position, int]]: A list containing pairs of Position and the id of the agent there
        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def extend_plans(self, extensions: List[Tuple[int, List[Tuple[Position, int]]]]) -> None:
        """
        Abstract method to extend plans of agents without changing existing plans
        TODO: Consider changing incomplete plans? Commit windows...

        Args:
            extensions:
                List[Tuple[int, List[Tuple[Position, int]]]]: A list containing pairs of agent_id and plan extensions,
                                                                where plan extensions are tuples of Position and timestep to reach it  
        """
        